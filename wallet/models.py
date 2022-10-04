
from random import choices
from django.db import models
from django.contrib.postgres.fields import ArrayField



# Create your models here.

class Customer(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    address=models.TextField()
    age=models.PositiveSmallIntegerField()
    nationallity=models.CharField(max_length=20)
    email=models.EmailField()
    id_number=models.CharField(max_length=20)
    profile_picture=models.ImageField(upload_to='images/',null=True)
    MARITAL_CHOICES =(
    ("Married", "Married"),
    ("Single", "Single"),
    )
    marital_status=models.CharField(max_length=10, choices=MARITAL_CHOICES)
    signature=models.ImageField(null=True)
    occupation=models.CharField(max_length=20)
    employed=models.BooleanField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.first_name



class Currency(models.Model):
    CURRENCY_CHOICES =(
        ('Ksh','Ksh'),
        ('USh','USh'),
        ('SDG','SDG'),
        ('TSh','TSh'),
        ('SR','SR'),
        ('Ar','Ar'),
        ('FRw','FRw'),
        ('K','K'), 
        ('SR','SR'),
        ('Br' ,'Br' ),
        
    )
    symbol=models.CharField(max_length=5,choices=CURRENCY_CHOICES)
    NAME_CHOICES =(
        ('KenyaShilling','KenyaShilling'),
        ('UgandaShillings','UgandaShillings'),
        ('Pound','Pound'),
        ('TanzaniaShillings','TanzaniaShillings'),
        ('SomaliaShillings','SomaliaShillings'),
        ('Malagasy ariary' ,'Malagasy ariary' ),
        ('Franc','Franc'),
        ('Kwacha','Kwacha'), 
        ('Rupees','Rupees'),
        ('Birr','Birr'),
        
    )
    name=models.CharField(max_length=30,choices=NAME_CHOICES)
    country=models.CharField(max_length=20)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Wallet(models.Model):
    currency=models.ForeignKey(Currency,on_delete=models.CASCADE)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    balance=models.DecimalField(max_digits=19,decimal_places=2)
    date_created=models.DateTimeField(auto_now_add=True)
    pin=models.CharField(max_length=5)
    is_active=models.BooleanField()
    WALLET_CHOICES =(
    ("business","Business"),
    ("family","Family"),
    ("custodial","Custodial"),
    ("fees","Fees"),
    ("salary","Salary"),
    ("savings","Savings"),
    ("retirement","Retirment")
    )
    wallet_type=models.CharField(max_length=15,choices=WALLET_CHOICES)
    def __str__(self):
        """Return a string representation of the model."""
        return self.customer.first_name

class Account(models.Model):
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    name_wallet=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    acc_number=models.IntegerField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.name_wallet.first_name 


class Receipt(models.Model):
    receipt_name=models.CharField(max_length=20)
    receipt_date=models.DateTimeField(auto_now_add=True)
    receipt_file=models.FileField(upload_to='media/')
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.receipt_name

class Third_party(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    name_thirdparty=models.CharField(max_length=20)
    id_thirdparty=models.CharField(max_length=15)
    email_thirdparty=models.EmailField()
    phonenumber_thirdparty=models.CharField(max_length=20)
    isactive_thiirdparty=models.BooleanField()
    transaction_thirdparty=models.IntegerField()
    currency_thirdparty=models.ForeignKey(Currency,on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name_thirdparty

class Transactions(models.Model):
    transaction_code=models.CharField(max_length=20)
    wallet_trans=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    transaction_amount=models.IntegerField()
    TRANSACTION_CHOICE=(
        ("credit","Credit"),
        ("debit","Debit")
    )
    transaction_type=models.CharField(max_length=10,choices=TRANSACTION_CHOICE)
    transaction_datetime=models.DateTimeField(null=True)
    receipt=models.OneToOneField(Receipt,on_delete=models.CASCADE)
    origin_acc=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='origin_acc',null=True)
    destination_acc=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='destination_acc')
    # third_party=models.ForeignKey(Third_party,on_delete=models.CASCADE)
    transaction_cost=models.IntegerField()
    status=ArrayField(
        models.CharField(max_length=50,blank=True),size=3) 
    transaction_type=models.CharField(max_length=10)

    def __str__(self):
        """Return a string representation of the model."""
        return self.transaction_type



class Card(models.Model):
    date_issed=models.DateField(auto_now_add=True)
    card_name=models.CharField(max_length=20)
    card_number=models.IntegerField()
    CARD_CHOICE=(
        ("credit","Credit"),
        ("debit","Debit")
    )
    card_type=models.CharField(max_length=10,choices=CARD_CHOICE)
    expiry_date=models.DateField()
    cvv_code=models.CharField(max_length=10)
    account_card=models.ForeignKey(Account,on_delete=models.CASCADE)
    ISSUER_CHOICE=(
        ("visa","Visa"),
        ("master","Master")
    )
    issuer=models.CharField(max_length=10,choices=ISSUER_CHOICE)
    signature_card=models.ImageField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.issuer

class Notifications(models.Model):
    id_notification=models.IntegerField()
    name_notification=models.CharField(max_length=15)
    status=ArrayField(
        models.CharField(max_length=10)
    )
    datetime_created=models.DateTimeField(auto_now_add=True)
    message  =models.TextField()
    recipient=models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__(self):
            """Return a string representation of the model."""
            return self.name_notification

class Loan(models.Model):
    loan_number=models.IntegerField()
    LOAN_CHOICES =(
    ("business","Business"),
    ("student","STudent"),
    ("home equity","Home Equity"),
    ("mortgage","Mortgage"),
    ("car","Car"),
    ("personal","Personal")
    )
    loan_type=models.CharField(max_length=15,choices=LOAN_CHOICES)
    loan_amount=models.IntegerField()
    datetime_loan=models.DateTimeField(auto_now_add=True)
    wallet_loan=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    Interest_rate=models.IntegerField()
    guarantee=models.ForeignKey(Third_party,on_delete=models.CASCADE)
    payment_due_date=models.DateField()
    loan_balance=models.IntegerField()
    loan_terms=models.TextField()
    duration=models.IntegerField()
    status=ArrayField(
        models.CharField(max_length=50,blank=True),size=3)


    def __str__(self):
        """Return a string representation of the model."""
        return self.loan_type

class Reward(models.Model):
    transaction_reward=models.ForeignKey(Transactions,on_delete=models.CASCADE)
    wallet_reward=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    datetime_reward=models.DateTimeField(auto_now_add=True)
    bonus_oints=models.IntegerField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.transaction_reward.transaction_code



    




    


