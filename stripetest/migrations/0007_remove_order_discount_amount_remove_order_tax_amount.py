# Generated by Django 4.0.5 on 2023-03-03 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stripetest', '0006_order_tax_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tax_amount',
        ),
    ]