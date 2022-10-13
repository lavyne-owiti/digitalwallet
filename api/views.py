# from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Account, Card, Customer, Loan, Notifications, Receipt, Transactions, Wallet
from .serializer import AccountSerializer, CardSerializer, CustomerSerializer, LoanSerializer, NotificationSerializer, ReceiptSerializer, TransactionSerializer, WalletSerializer


# Create your views here.
class CustomerViewsets(viewsets.ModelViewSet):   
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class WalletViewsets(viewsets.ModelViewSet):   
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer

class AccountViewsets(viewsets.ModelViewSet):   
    queryset=Account.objects.all()
    serializer_class=AccountSerializer

class CardViewsets(viewsets.ModelViewSet):   
    queryset=Card.objects.all()
    serializer_class=CardSerializer

class TransactionViewsets(viewsets.ModelViewSet):   
    queryset=Transactions.objects.all()
    serializer_class=TransactionSerializer

class LoanViewsets(viewsets.ModelViewSet):   
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer

class ReceiptViewsets(viewsets.ModelViewSet):   
    queryset=Receipt.objects.all()
    serializer_class=ReceiptSerializer

class NotificationViewsets(viewsets.ModelViewSet):   
    queryset=Notifications.objects.all()
    serializer_class=NotificationSerializer