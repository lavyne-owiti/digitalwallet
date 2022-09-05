from django.urls import path 
from .views import account_add, card_add, curency_add, loan_add, notification_add, receipt_add, register_customer, reward_add, thirdparty_add, transaction_add, wallet_add

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

]