from tkinter import W
from django.shortcuts import render
from django.shortcuts import redirect

from wallet.models import Account, Card, Customer, Receipt, Transactions, Wallet
from .forms import AccountForm, CardForm, CurrencyForm, CustomerRegistrationForm, LoanForm, ReceiptForm, RewardForm, ThirdpartyForm, TransactionForm, WalletForm

# Create your views here.
def register_customer(request):
    if request.method =="POST":
        form = CustomerRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{'form':form})

def curency_add(request):
    if request.method =="POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CurrencyForm()
    return render(request,"wallet/currency_add.html",{'form':form})

def wallet_add(request):
    if request.method =="POST":
        form = WalletForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= WalletForm()
    return render(request,"wallet/wallet_add.html",{'form':form})

def account_add(request):
    if request.method =="POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= AccountForm()
    return render(request,"wallet/account_add.html",{'form':form})  

def card_add(request):
    form= CardForm()
    return render(request,"wallet/card_add.html",{'form':form})  

def loan_add(request):
    if request.method =="POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= LoanForm()
    return render(request,"wallet/loan_add.html",{'form':form})  

def transaction_add(request):
    if request.method =="POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= TransactionForm()
    return render(request,"wallet/transaction_add.html",{'form':form})  

def reward_add(request):
    if request.method =="POST":
        form = RewardForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= RewardForm()
    return render(request,"wallet/reward_add.html",{'form':form})  

def receipt_add(request):
    if request.method =="POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= ReceiptForm()
    return render(request,"wallet/receipt_add.html",{'form':form})  

def notification_add(request):
    if request.method =="POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= AccountForm()
    return render(request,"wallet/account_add.html",{'form':form})  

def thirdparty_add(request):
    if request.method =="POST":
        form = ThirdpartyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= ThirdpartyForm()
    return render(request,"wallet/thirdparty_add.html",{'form':form})  

def list_customers(request):
    if request.method =="POST":
        form = Customer(request.POST)
        if form.is_valid():
            form.save()
    else:
        customers=Customer.objects.all()
    return render(request,"wallet/list_customer.html",{'customers':customers})  

def customer_profile(request,id):
    customer=Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{'customer':customer})

def edit_customer(request,id):
    customer=Customer.objects.get(id=id)
    if request.method =='POST':
        form = CustomerRegistrationForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect(request,"customer_profile",id=customer.id)
    else:
        form = CustomerRegistrationForm()
        return render(request,"wallet/edit_customer.html",{'form':form})

def list_wallet(request):
    if request.method =="POST":
        form =  Wallet(request.POST)
        if form.is_valid():
            form.save()
    else:
        customers= Wallet.objects.all()
    return render(request,"wallet/list_wallet.html",{'customers':customers})  

def wallet_profile(request,id):
    customer=Wallet.objects.get(id=id)
    return render(request,"wallet/wallet_profile.html",{'customer':customer})

def edit_wallet(request,id):
    customer=Wallet.objects.get(id=id)
    if request.method =='POST':
        form = WalletForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect(request,"wallet_profile",id=customer.id)
    else:
        form = WalletForm()
        return render(request,"wallet/edit_wallet.html",{'form':form})

def list_account(request):
    if request.method =="POST":
        form =  Account(request.POST)
        if form.is_valid():
            form.save()
    else:
        customers= Account.objects.all()
    return render(request,"wallet/list_account.html",{'customers':customers})  

def account_profile(request,id):
    customer=Account.objects.get(id=id)
    return render(request,"wallet/account_profile.html",{'customer':customer})

def edit_account(request,id):
    customer=Account.objects.get(id=id)
    if request.method =='POST':
        form = AccountForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect(request,"account_profile",id=customer.id)
    else:
        form = AccountForm()
        return render(request,"wallet/edit_account.html",{'form':form})
 
def list_card(request):
    if request.method =="POST":
        form =  Card(request.POST)
        if form.is_valid():
            form.save()
    else:
        customers= Card.objects.all()
    return render(request,"wallet/list_card.html",{'customers':customers})  

def card_profile(request,id):
    customer=Card.objects.get(id=id)
    return render(request,"wallet/card_profile.html",{'customer':customer})

def edit_card(request,id):
    customer=Card.objects.get(id=id)
    if request.method =='POST':
        form = CardForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect(request,"card_profile",id=customer.id)
    else:
        form = CardForm()
        return render(request,"wallet/edit_card.html",{'form':form})
 
def list_transaction(request):
    if request.method =="POST":
        form =  Transactions(request.POST)
        if form.is_valid():
            form.save()
    else:
        customers= Transactions.objects.all()
    return render(request,"wallet/list_transaction.html",{'customers':customers})  

def transaction_profile(request,id):
    customer=Transactions.objects.get(id=id)
    return render(request,"wallet/transaction_profile.html",{'customer':customer})

def edit_transaction(request,id):
    customer=Transactions.objects.get(id=id)
    if request.method =='POST':
        form = TransactionForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect(request,"transaction_profile",id=customer.id)
    else:
        form = TransactionForm()
        return render(request,"wallet/edit_transaction.html",{'form':form})

def list_receipt(request):
    if request.method =="POST":
        form =  Receipt(request.POST)
        if form.is_valid():
            form.save()
    else:
        customers= Receipt.objects.all()
    return render(request,"wallet/list_receipt.html",{'customers':customers})  

def receipt_profile(request,id):
    customer=Receipt.objects.get(id=id)
    return render(request,"wallet/receipt_profile.html",{'customer':customer})

def edit_receipt(request,id):
    customer=Receipt.objects.get(id=id)
    if request.method =='POST':
        form = ReceiptForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect(request,"receipt_profile",id=customer.id)
    else:
        form = ReceiptForm()
        return render(request,"wallet/edit_receipt.html",{'form':form})