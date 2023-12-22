from django.urls import path
from .views import products_view, shop_view, products_page_view, cart_view, cart_add_view, cart_del_view

app_name = 'store'

urlpatterns = [
    path('product/', products_view),
    path('', shop_view),
    path('product/<slug:page>.html', products_page_view),
    path('product/<int:page>', products_page_view, name="product_page_view"),
    path('cart/', cart_view),
    path('cart/add/<str:id_product>', cart_add_view),
    path('cart/del/<str:id_product>', cart_del_view),
    ]