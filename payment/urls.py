from django.urls import path
from . import views

urlpatterns = [
    path('donate', views.donate, name='donate'),
    path('make_payment/<str:ref>/', views.verify_payment, name='verify-payment'),
    path('verification-success/', views.verification_success, name='verification-success'),
    path('verification-failed/', views.verification_failed, name='verification-failed'),
]