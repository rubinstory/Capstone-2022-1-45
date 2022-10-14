# Generated by Django 4.0.6 on 2022-08-23 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, unique=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank.bank')),
            ],
        ),
    ]