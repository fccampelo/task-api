# Generated by Django 2.0 on 2017-12-08 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0004_contract_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='user',
            new_name='contract',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='date_field',
            new_name='date_payment',
        ),
    ]
