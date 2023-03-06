# Generated by Django 4.0.5 on 2023-03-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripetest', '0002_discount_tax_alter_item_price_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount_percent',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='tax',
            name='tax_percent',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]