from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('service_request/', views.submit_service_request, name='submit_request'),
    path('track_request/', views.track_request_status, name='track_request'),
    path('request_submitted/', views.request_submitted, name='request_submitted'),
    path('bill/<int:request_id>/pdf/', views.generate_bill_pdf, name='generate_bill_pdf'),
]
