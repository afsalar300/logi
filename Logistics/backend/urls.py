from django.urls import path
from backend import views

urlpatterns = [
    path('bindex/', views.bindex, name='bindex'),
    path('status/', views.status, name='status'),
    path('statusEdit/<int:dataid>/', views.statusEdit, name='statusEdit'),
    path('updatestatus/<int:dataid>', views.updatestatus, name='updatestatus'),
    path('message/', views.message, name='message'),
    path('sender/', views.sender, name='sender'),
    path('recever/', views.recever, name='recever'),
    ]
