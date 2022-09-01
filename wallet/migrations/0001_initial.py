# Generated by Django 4.0.6 on 2022-08-25 07:50

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(choices=[('Ksh', 'Ksh'), ('USh', 'USh'), ('SDG', 'SDG'), ('TSh', 'TSh'), ('SR', 'SR'), ('Ar', 'Ar'), ('FRw', 'FRw'), ('K', 'K'), ('SR', 'SR'), ('Br', 'Br')], max_length=5)),
                ('name', models.CharField(choices=[('KenyaShilling', 'KenyaShilling'), ('UgandaShillings', 'UgandaShillings'), ('Pound', 'Pound'), ('TanzaniaShillings', 'TanzaniaShillings'), ('SomaliaShillings', 'SomaliaShillings'), ('Malagasy ariary', 'Malagasy ariary'), ('Franc', 'Franc'), ('Kwacha', 'Kwacha'), ('Rupees', 'Rupees'), ('Birr', 'Birr')], max_length=30)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('address', models.TextField()),
                ('age', models.PositiveSmallIntegerField()),
                ('nationallity', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('id_number', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(upload_to='images/')),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], max_length=10)),
                ('signature', models.ImageField(upload_to='')),
                ('occupation', models.CharField(max_length=20)),
                ('employed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateTimeField(auto_now_add=True)),
                ('receipt_file', models.FileField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=19)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('pin', models.CharField(max_length=5)),
                ('is_active', models.BooleanField()),
                ('wallet_type', models.CharField(choices=[('business', 'Business'), ('family', 'Family'), ('custodial', 'Custodial'), ('fees', 'Fees'), ('salary', 'Salary'), ('savings', 'Savings'), ('retirement', 'Retirment')], max_length=15)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.currency')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(max_length=20)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_datetime', models.DateTimeField(null=True)),
                ('transaction_cost', models.IntegerField()),
                ('status', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), size=3)),
                ('transaction_type', models.CharField(max_length=10)),
                ('destination_acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
                ('receipt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wallet.receipt')),
                ('wallet_trans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Third_party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_thirdparty', models.CharField(max_length=20)),
                ('id_thirdparty', models.CharField(max_length=15)),
                ('email_thirdparty', models.EmailField(max_length=254)),
                ('phonenumber_thirdparty', models.CharField(max_length=20)),
                ('isactive_thiirdparty', models.BooleanField()),
                ('transaction_thirdparty', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
                ('currency_thirdparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_reward', models.DateTimeField(auto_now_add=True)),
                ('bonus_oints', models.IntegerField()),
                ('transaction_reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.transactions')),
                ('wallet_reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_notification', models.IntegerField()),
                ('name_notification', models.CharField(max_length=15)),
                ('status', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_number', models.IntegerField()),
                ('loan_type', models.CharField(choices=[('business', 'Business'), ('student', 'STudent'), ('home equity', 'Home Equity'), ('mortgage', 'Mortgage'), ('car', 'Car'), ('personal', 'Personal')], max_length=15)),
                ('loan_amount', models.IntegerField()),
                ('datetime_loan', models.DateTimeField(auto_now_add=True)),
                ('Interest_rate', models.IntegerField()),
                ('payment_due_date', models.DateField()),
                ('loan_balance', models.IntegerField()),
                ('loan_terms', models.TextField()),
                ('duration', models.IntegerField()),
                ('status', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), size=3)),
                ('guarantee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.third_party')),
                ('wallet_loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issed', models.DateField(auto_now_add=True)),
                ('card_name', models.CharField(max_length=20)),
                ('card_number', models.IntegerField()),
                ('card_type', models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], max_length=10)),
                ('expiry_date', models.DateField()),
                ('cvv_code', models.CharField(max_length=10)),
                ('issuer', models.CharField(choices=[('visa', 'Visa'), ('master', 'Master')], max_length=10)),
                ('signature_card', models.ImageField(upload_to='')),
                ('account_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='name_wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.customer'),
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet'),
        ),
    ]
