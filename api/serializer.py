
from rest_framework import serializers
from wallet.models import Account, Card, Customer, Loan, Notifications, Receipt, Transactions, Wallet

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("first_name","age","email")

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields=("currency","customer","wallet_type") 

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=("wallet","name_wallet","acc_number")

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields=("card_type"," issuer","account_card")

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transactions
        fields=("wallet_trans"," origin_acc","destination_acc","transaction_type")

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields=("wallet_loan","loan_type","loan_terms")

class  ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Receipt
        fields=("receipt_name","receipt_date")

class  NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notifications
        fields=("recipient","message","name_notification")
