from . import views
from django.urls import path
app_name='cart_app'

urlpatterns = [
    path('',views.cart_id,name="cart_id"),
    path('add/<int:product_id>/',views.add_cart,name="add_cart"),
    path('detail/',views.cart_detail,name="cart_detail"),
    path('remove/<int:product_id>/', views.cart_remove, name="cart_remove"),
    path('full_remove/<int:product_id>/', views.full_remove, name="full_remove")


]