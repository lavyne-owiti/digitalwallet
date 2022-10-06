from unicodedata import name
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import account_add, account_profile, card_add, curency_add, customer_profile, edit_account, edit_customer, edit_receipt, edit_transaction, edit_wallet, list_account, list_customers, list_receipt, list_transaction, list_wallet, loan_add, notification_add, receipt_add, receipt_profile, register_customer, reward_add, thirdparty_add, transaction_add, transaction_profile, wallet_add, wallet_profile

urlpatterns=[
    
    path('register/',register_customer,name="registration"),
    path('currency/',curency_add,name='currencies'),
    path('wallets/',wallet_add,name='walletss'),
    path('account/',account_add,name='accounts'),
    path('card/',card_add,name='cards'),
    path('loan/',loan_add,name='loans'),
    path('notification/',notification_add,name='notifications'),
    path('receipt/',receipt_add,name='receipts'),
    path('reward/',reward_add,name='rewards'),
    path('thirdparty/',thirdparty_add,name='thirdpartys'),
    path('transaction/',transaction_add,name='transactions'),

    path('list/',list_customers,name="lists"),
    path('listwallet/',list_wallet,name="listwallet"),
    path('listaccount/',list_account,name="listaccount"),
    path('listtransaction/',list_transaction,name="listaccount"),
    path('listreceipt/',list_receipt,name="listreceipt"),

    path('customers/<int:id>/',customer_profile,name="customer_profile"),
    path('customers/<int:id>/',wallet_profile,name="customer_profile"),
    path('customers/<int:id>/',account_profile,name="account_profile"),
    path('customers/<int:id>/',transaction_profile,name="transaction_profile"),
    path('customers/<int:id>/',receipt_profile,name="receipt_profile"),

    path('customers/edit/<int:id>/',edit_customer,name="edit_customer"),
    path('customers/edit/<int:id>/',edit_wallet,name="edit_customer"),
    path('customers/edit/<int:id>/',edit_account,name="edit_account"),
    path('customers/edit/<int:id>/',edit_transaction,name="edit_transaction"),
    path('customers/edit/<int:id>/',edit_receipt,name="edit_receipt"),
    



]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)