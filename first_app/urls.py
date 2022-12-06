# from django.conf.urls import ulr  {{{DONT NEED IT FROM VIDEO}}}
from django.urls import path
from first_app import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('form/', views.form, name= 'form')
    # path('home/', views.index, name = 'index'),
    # path('about/', views.about, name = 'about'),
    # path('contact/', views.contact, name = 'contact'),
]