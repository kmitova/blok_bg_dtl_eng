from django.contrib import admin

from payment.models import Payment, Fee


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    pass