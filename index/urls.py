from django.urls import path
from . import views
urlpatterns = [

    path('home/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('skills/',views.skills,name='skills'),
    path('register/',views.userRegister,name='register'),

    path('',views.userLogin,name='login'),
    path('logout/',views.logoutUser,name='logout')
    

]