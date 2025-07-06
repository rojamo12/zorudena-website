import uuid
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
from .utils import generate_transaction_reference  # Transaction ref generator


def dpo_payment(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name', 'John Doe')
        email = request.POST.get('email', 'john@example.com')
        phone = request.POST.get('phone', '+254700000000')
        amount = request.POST.get('amount', '100.00')
        currency = "USD"

        if not full_name or not email or not phone or not amount:
            return HttpResponseBadRequest("Missing required fields")

        try:
            amount = float(amount)
        except ValueError:
            return HttpResponseBadRequest("Invalid amount")

        txn_ref = generate_transaction_reference()

        Payment.objects.create(
            reference=txn_ref,
            full_name=full_name,
            email=email,
            phone=phone,
            amount=amount,
            currency=currency,
            status='pending'
        )

        ngrok_url = "https://7558-41-210-145-80.ngrok-free.app"

        name_parts = full_name.split()
        first_name = name_parts[0]
        last_name = name_parts[-1]

        post_data = {
            "companyToken": settings.DPO_COMPANY_TOKEN,
            "serviceType": settings.DPO_SERVICE_TYPE,
            "transactionReference": txn_ref,
            "customerFirstName": first_name,
            "customerLastName": last_name,
            "customerEmail": email,
            "customerPhone": phone,
            "amount": amount,
            "currency": currency,
            "redirectURL": f"{ngrok_url}/payment-success/",
            "cancelURL": f"{ngrok_url}/payment-cancel/",
        }

        return render(request, 'payments/dpo_form.html', {"data": post_data})

    # Show payment form on GET
    return render(request, 'payments/payment_form.html')


def payment_success(request):
    txn_ref = request.GET.get("TransactionReference")
    if txn_ref:
        payment = Payment.objects.filter(reference=txn_ref).first()
        if payment:
            payment.status = "success"
            payment.save()
    return render(request, 'payments/success.html')


def payment_cancel(request):
    txn_ref = request.GET.get("TransactionReference")
    if txn_ref:
        payment = Payment.objects.filter(reference=txn_ref).first()
        if payment:
            payment.status = "failed"
            payment.save()
    return render(request, 'payments/cancel.html')


@csrf_exempt
def dpo_ipn_listener(request):
    if request.method == "POST":
        txn_ref = request.POST.get("TransactionReference")
        status = request.POST.get("TransactionStatus")

        payment = Payment.objects.filter(reference=txn_ref).first()
        if payment and status == "Success":
            payment.status = "success"
            payment.save()
        return HttpResponse("OK")

    return HttpResponseBadRequest("Invalid method")
