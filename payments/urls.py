from django.urls import path
from . import views

urlpatterns = [
    path('make-payment/', views.dpo_payment, name='make_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
    path('dpo-ipn/', views.dpo_ipn_listener, name='dpo_ipn'),
]



