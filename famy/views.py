from django.shortcuts import render,get_object_or_404,redirect
from .models import  Photo,Category
from django.core.mail import send_mail
from .forms import ContactForm

from django.contrib.auth import authenticate, login





def index(request):
    return render(request, 'famy/base.html')

def home(request):
    
    return render(request, 'famy/home.html')


def about(request):
    return render(request, 'famy/about.html')



def family_member_detail(request):
    
    return render(request, 'famy/family_member.html')






# views.py



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\n\nMessage: {message}',
                'your_email@example.com',
                ['stalwartekwere@gmail.com'],  # Replace with your desired recipient(s)
                fail_silently=False,
            )
            return render(request, 'famy/success.html')  # Render a success page after email is sent
    else:
        form = ContactForm()
    return render(request, 'famy/contact.html', {'form': form})




def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, "famy/gallery.html", context)

def photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    return render(request, "famy/photo.html", {'photo': photo})

def add_photo(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get("image")

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != "":
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )

    context = {"categories": categories}
    return render(request, 'famy/add.html', context)


def LoginView(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # If the user is authenticated, log them in
                login(request, user)
                return redirect('famy:add' )  # Redirect to the 'add' page after successful login
            else:
                return render(request, 'famy/login.html', {'error': 'Invalid username or password'})

        else:
            return render(request, 'famy/login.html', {'error': 'Please fill in all fields'})

    return render(request, 'famy/login.html')

