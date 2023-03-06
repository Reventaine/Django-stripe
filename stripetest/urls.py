from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('buy/<int:item_id>/', views.buy_item, name='create_checkout_session'),
    path('create_order', views.create_order, name='create_order'),
    path('order/<int:order_id>/', views.view_order, name='order'),
    path('buy_order/<int:order_id>/', views.buy_order, name='create_checkout_session'),
    # path('create-payment-intent/<int:order_id>/', views.create_payment_intent, name='create_payment_intent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




