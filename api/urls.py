from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.productView),
    path('products/info/', views.productInfoView),
    path ('products/<int:pk>', views.productDetails),

    path('orders/', views.orderView)

]
