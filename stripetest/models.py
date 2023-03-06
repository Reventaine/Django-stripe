from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # currency = models.CharField(max_length=3, choices=[('USD', '$'), ('EUR', '€')])

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=100)
    discount_percent = models.DecimalField(max_digits=2, decimal_places=1)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=100)
    tax_percent = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100, help_text=f'Order name here...')
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def calculate_total_amount(self):
        total = sum([item.price for item in self.items.all()])
        if self.discount:
            total *= (100 - self.discount.discount_percent) / 100
        if self.tax:
            total *= (100 + self.tax.tax_percent) / 100
        self.total_amount = total
        self.save()

    """def create_payment_intent(self):
        import stripe
        stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

        metadata = {
            "order_id": str(self.pk),
            "total_amount": str(self.total_amount),
        }

        payment_intent = stripe.PaymentIntent.create(
            amount=int(self.total_amount * 100),
            currency="usd",
            payment_method_types=["card"],
            metadata=metadata,
        )
        print(payment_intent)
        return payment_intent"""

    def __str__(self):
        self.save()
        return self.name






