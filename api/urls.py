from django.urls import path,include
from rest_framework import routers
from .views import AccountViewsets, CardViewsets, CustomerViewsets, LoanViewsets, NotificationViewsets, ReceiptViewsets, TransactionViewsets, WalletViewsets


router=routers.DefaultRouter()
router.register(r'customers',CustomerViewsets)
router.register(r'wallets',WalletViewsets)
router.register(r'accounts',AccountViewsets)
router.register(r'cards',CardViewsets)
router.register(r'transactions',TransactionViewsets)
router.register(r'loans',LoanViewsets)
router.register(r'receipts',ReceiptViewsets)
router.register(r'notifications',NotificationViewsets)

urlpatterns=[
    path('',include(router.urls)),
]