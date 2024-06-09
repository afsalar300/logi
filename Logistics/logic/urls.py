from django.contrib import admin
from django.urls import path

from logic import views

urlpatterns = [
     path('index/', views.index, name='index'),
     path('login/', views.login, name='login'),
     path('home/', views.home, name='home'),
     path('savelog/', views.savelog, name='savelog'),
     path('loginsave/', views.loginsave, name='loginsave'),
     path('logout/', views.logout, name='logout'),
     path('detail/', views.detail, name='detail'),

     path('home/', views.home, name='home'),
     path('senderdata/', views.senderdata, name='senderdata'),
     path('home2/', views.home2, name='home2'),
     path('receiverdata/', views.receiverdata, name='receiverdata'),
     path('first/', views.first, name='first'),

     path('about/', views.about, name='about'),

     path('service/', views.service, name='service'),
     path('orders/', views.orders, name='orders'),
     # path('edit/<int:dataid>/', views.edit, name='edit'),
     path('editupdate2/<int:dataid>/', views.editupdate2, name='editupdate2'),
     path('delete/<int:de>/', views.delete, name='delete'),
     path('edit2/<int:dataid>/', views.edit2, name='edit2'),
     path('profiledb/', views.profiledb, name='profiledb'),
     path('profilecreate/', views.profilecreate, name='profilecreate'),

     path('contact/', views.contact, name='contact'),
     path('contactdata/', views.contactdata, name='contactdata'),


]