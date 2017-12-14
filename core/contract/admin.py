from django.contrib import admin

from contract.models import Contract, Payment
# Register your models here.
class ContractAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'description', 'amount')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('contract', 'value', 'date_payment')

admin.site.register(Contract, ContractAdmin)
admin.site.register(Payment, PaymentAdmin)
