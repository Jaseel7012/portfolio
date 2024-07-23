from django.urls import path
from . import views
urlpatterns = [

    path('create/',views.create),
    path('view/',views.list_detail,name='list')
    ]