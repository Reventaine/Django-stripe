# Generated by Django 4.0.5 on 2023-03-03 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripetest', '0007_remove_order_discount_amount_remove_order_tax_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='Order', max_length=100),
        ),
    ]
