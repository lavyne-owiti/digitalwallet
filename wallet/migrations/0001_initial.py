# Generated by Django 4.0.6 on 2022-07-30 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=1)),
                ('address', models.TextField()),
                ('age', models.PositiveSmallIntegerField()),
                ('nationallity', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('id_number', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(upload_to='images/')),
                ('marital_status', models.CharField(max_length=15)),
                ('signature', models.ImageField(upload_to='')),
                ('occupation', models.CharField(max_length=20)),
                ('employed', models.BooleanField()),
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
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.currency')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
    ]
