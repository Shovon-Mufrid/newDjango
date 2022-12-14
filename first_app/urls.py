# from django.conf.urls import ulr  {{{DONT NEED IT FROM VIDEO}}}
from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [

    path('', views.index, name = 'index'),
    path('album_list/', views.album_list, name = 'album_list'),
    path('album_list/<int:artist_id>/', views.album_list, name = 'album_list'),
    path('musician_form/', views.musician_form, name = 'musician_form'),
    path('album_form/', views.album_form, name = 'album_form'),
    path('edit_artist/', views.edit_artist, name = 'edit_artist'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name = 'edit_artist'),
    path('edit_album/', views.edit_album, name = 'edit_album'),
    path('edit_album/<int:album_id>/', views.edit_album, name = 'edit_album'),
    path('delete_album/', views.delete_album, name='delete_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_artist/', views.delete_musician, name='delete_musician'),
    path('delete_artist/<int:artist_id>/', views.delete_musician, name='delete_musician'),
   








    # # rmv from vid 8.2
    # path('', views.index, name = 'index'),
    # path('form/', views.form, name= 'form'),
    # path('contact/', views.contact, name= 'contact'),


    # path('home/', views.index, name = 'index'),
    # path('about/', views.about, name = 'about'),
    # path('contact/', views.contact, name = 'contact'),
]