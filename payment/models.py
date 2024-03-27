from django.db import models
import secrets

from django.urls import reverse
from .paystack import PayStack

# Create your models here.


class Payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.PositiveBigIntegerField()
    phone = models.CharField(max_length=14, null=True)
    country = models.CharField(max_length=14, null=True)
    ref = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return f"Payment: {self.amount}"

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return self.amount * 101

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 101 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False
    

class PaymentOption(models.Model):
    fullname = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_amount = models.PositiveBigIntegerField()
    user_phone = models.CharField(max_length=14, null=True)
    payment_option = models.CharField(max_length=50, null=True)
    user_country = models.CharField(max_length=14, null=True)
    date_donated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'payment option'
        ordering = ['-date_donated']
    
    def __str__(self):
        return f"Payment: {self.user_amount}"