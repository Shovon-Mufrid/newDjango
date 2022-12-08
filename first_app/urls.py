# from django.conf.urls import ulr  {{{DONT NEED IT FROM VIDEO}}}
from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [

    path('', views.index, name = 'index'),
    path('album_list/', views.album_list, name = 'album_list'),
    path('musician_form/', views.musician_form, name = 'musician_form'),
    path('album_form/', views.album_form, name = 'album_form'),
   








    # # rmv from vid 8.2
    # path('', views.index, name = 'index'),
    # path('form/', views.form, name= 'form'),
    # path('contact/', views.contact, name= 'contact'),


    # path('home/', views.index, name = 'index'),
    # path('about/', views.about, name = 'about'),
    # path('contact/', views.contact, name = 'contact'),
]