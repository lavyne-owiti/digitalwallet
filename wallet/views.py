from django.shortcuts import render
from .forms import AccountForm, CardForm, CurrencyForm, CustomerRegistrationForm, LoanForm, ReceiptForm, RewardForm, ThirdpartyForm, TransactionForm, WalletForm

# Create your views here.
def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{'form':form})

def curency_add(request):
    form = CurrencyForm()
    return render(request,"wallet/currency_add.html",{'form':form})

def wallet_add(request):
    form= WalletForm()
    return render(request,"wallet/wallet_add.html",{'form':form})

def account_add(request):
    form= AccountForm()
    return render(request,"wallet/account_add.html",{'form':form})  

def card_add(request):
    form= CardForm()
    return render(request,"wallet/card_add.html",{'form':form})  

def loan_add(request):
    form= LoanForm()
    return render(request,"wallet/loan_add.html",{'form':form})  

def transaction_add(request):
    form= TransactionForm()
    return render(request,"wallet/transaction_add.html",{'form':form})  

def reward_add(request):
    form= RewardForm()
    return render(request,"wallet/reward_add.html",{'form':form})  

def receipt_add(request):
    form= ReceiptForm()
    return render(request,"wallet/receipt_add.html",{'form':form})  

def notification_add(request):
    form= AccountForm()
    return render(request,"wallet/account_add.html",{'form':form})  

def thirdparty_add(request):
    form= ThirdpartyForm()
    return render(request,"wallet/thirdparty_add.html",{'form':form})  

