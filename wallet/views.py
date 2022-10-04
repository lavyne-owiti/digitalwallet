from django.shortcuts import render
from django.shortcuts import redirect

from wallet.models import Customer
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
        form = ThirdpartyForm(request.POST)
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

    

 