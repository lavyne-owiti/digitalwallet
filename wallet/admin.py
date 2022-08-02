from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notifications, Receipt, Reward, Third_party, Transactions
from .models import Currency
from .models import Wallet

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display =('first_name','last_name','email')
    search_fields =('firs_name','last_name')
    
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Currency)
admin.site.register(Transactions)
admin.site.register(Reward)
admin.site.register(Loan)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Third_party)
admin.site.register(Notifications)
admin.site.register(Receipt)
