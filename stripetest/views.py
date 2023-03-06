from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import stripe
import os

from .models import Item, Order, Tax, Discount
from .forms import OrderForm


stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_detail.html', {'item': item, 'stripe_public_key': stripe_public_key})


@csrf_exempt
def buy_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )

    return JsonResponse({'id': session.id})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.save()
            return redirect(reverse('order', kwargs={'order_id': order.pk}))
    else:
        form = OrderForm()
    items = Item.objects.all()
    discounts = Discount.objects.all()
    taxes = Tax.objects.all()
    return render(request, 'create_order.html', {'form': form, 'items': items, 'discounts': discounts, 'taxes': taxes})


def view_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.calculate_total_amount()
    return render(request, 'order.html', {'order': order, 'stripe_public_key': stripe_public_key})


@csrf_exempt
def buy_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': str(order.name),
                },
                'unit_amount': int(order.total_amount * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
        metadata={
            "order_id": str(order.pk),
            "total_amount": str(order.total_amount),
        }
    )

    return JsonResponse({'id': session.id})


"""def create_payment_intent(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if not order.total_amount:
        order.calculate_total_amount()

    payment_intent = order.create_payment_intent()

    print(payment_intent.client_secret)
    return JsonResponse({
        'client_secret': payment_intent.client_secret,
    })"""
