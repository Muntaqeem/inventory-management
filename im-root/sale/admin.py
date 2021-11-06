from django.contrib import admin
from .models import *
# Register your models here.

class paymentModel(admin.ModelAdmin):
    list_display = ('customer', 'supplier', 'debit_or_credit', 'amount', 'date', 'payment_type')
    list_filter = ('debit_or_credit', 'date', 'payment_type')
    search_fields = ['customer__name', 'supplier__name', 'bank__name']
    autocomplete_fields = ['customer', 'supplier', 'bank']

class saleAdmin(admin.ModelAdmin):
    list_display = ('name', 'invoice_no', 'payment_received_gt', 'payment_due_gt')
    list_filter = ('warehouse',)
    search_fields = ['invoice_no', 'name', 'address', 'contact']

class productAndQuantityAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'discount_in_percent')
    search_fields = ['product']
    autocomplete_fields = ['product']

admin.site.register(payments, paymentModel)
admin.site.register(sale, saleAdmin)
admin.site.register(productAndQuantity, productAndQuantityAdmin)
