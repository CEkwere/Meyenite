from django.urls import path
from . import views 


app_name = 'famy'

urlpatterns = [
   # home
    path('home/', views.home, name='home'),
    
    # about
    path('about/', views.about, name='about'),
    
    # contact
    path('contact/', views.contact, name='contact'),
    
    # family_member_detail
    path('family_member/', views.family_member_detail, name='family_member_detail'),
    
  
 


    path('gallery/', views.gallery, name='gallery'),
    path('photo/<int:photo_id>/', views.photo, name='photo'),
    path('add/', views.add_photo, name='add'),
    path('login/', views.LoginView, name='login'),    



]

    



