from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Payment, PaymentOption
from django.conf import settings
from django.http import HttpRequest
from django.contrib import messages
from .import forms


def donate(request: HttpRequest) -> HttpResponse:
    
    
    if request.method == 'POST':
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'payment/make_payment.html', {'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
        
    else:
        payment_form = forms.PaymentForm()

    if request.method == 'POST':
        fullname = request.POST['fullname']
        user_email = request.POST['user_email']
        user_amount = request.POST['user_amount']
        user_phone = request.POST['user_phone']
        user_country = request.POST['user_country']
        payment_option = request.POST['payment_option']
        donation = PaymentOption(fullname=fullname, user_email=user_email, user_amount=user_amount,
                                 user_phone=user_phone, payment_option=payment_option, user_country=user_country)
        donation.save()
        return redirect('donate')

    context = {
        'payment_form': payment_form,
        'title': 'Donate'
    }
    return render(request, 'payment/donate.html', context)


def verification_success(request):
    return render(request, 'payment/verification-success.html')


def verification_failed(request):
    return render(request, 'payment/verification-failed.html')


def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        return render(request, 'payment/verification-success.html')
    else:
        return render(request, 'payment/verification-failed.html')
