# Generated by Django 2.0 on 2017-12-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_auto_20171208_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('date_field', models.DateTimeField(auto_now_add=True, verbose_name='Data de pagamento')),
            ],
            options={
                'verbose_name': 'paymente',
                'verbose_name_plural': 'paymentes',
            },
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Contract', 'verbose_name_plural': 'Contracts'},
        ),
        migrations.AlterField(
            model_name='contract',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Titulo'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=True, related_name='contract', to='contract.Contract'),
        ),
    ]
