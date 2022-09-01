
from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notifications, Receipt, Reward, Third_party, Transactions
from .models import Currency
from .models import Wallet

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display =('first_name','last_name','email')
    search_fields =('firs_name','last_name')
class WalletAdmin(admin.ModelAdmin):
    list_display =('customer','wallet_type','is_active')
    search_fields =('customer','wallet_type')
class  CurrencyAdmin(admin.ModelAdmin):
    list_display =('country','name','symbol')
    search_fields =('country','name')
class TransactionsAdmin(admin.ModelAdmin):
    list_display =('wallet_trans','destination_acc','transaction_type')
    search_fields =('transaction_type','wallet_trans')
class  RewardAdmin(admin.ModelAdmin):
    list_display =('wallet_reward','datetime_reward')
    search_fields =('wallet_reward','datetime_reward')
class LoanAdmin(admin.ModelAdmin):
    list_display =('loan_type','guarantee','status')
    search_fields =('loan_type','guarantee')
class AccountAdmin(admin.ModelAdmin):
    list_display =('wallet','name_wallet')
    search_fields =('wallet','name_wallet')
class CardAdmin(admin.ModelAdmin):
    list_display =('card_name','card_type','issuer')
    search_fields =('card_name','issuer')
class Third_partyAdmin(admin.ModelAdmin):
    list_display =('name_thirdparty','email_thirdparty','account')
    search_fields =('name_thirdparty','account')
class ReceiptAdmin(admin.ModelAdmin):
    list_display =('receipt_date', 'receipt_file')
    search_fields =('receipt_date', 'receipt_file')
class NotificationAdmin(admin.ModelAdmin):
    list_display =('recipient','name_notification','datetime_created')
    search_fields =('recipient','name_notification')    

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Transactions,TransactionsAdmin)
admin.site.register(Reward,RewardAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(Third_party,Third_partyAdmin)
admin.site.register(Notifications,NotificationAdmin)
admin.site.register(Receipt,ReceiptAdmin)
