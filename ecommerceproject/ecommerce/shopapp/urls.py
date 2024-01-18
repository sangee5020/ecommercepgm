from . import views
from django.urls import path
app_name='shopapp'

urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('payment/',views.payment,name='payment'),
    path('<slug:c_slug>/',views.allprodcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodcatdetail'),

]
