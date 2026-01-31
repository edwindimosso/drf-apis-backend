from django.urls import path
from . import views


urlpatterns = [
    #products
    path('products/', views.ProductListView.as_view()),
    path('products/info/', views.productInfoView),
    path ('products/<int:pk>', views.productDetailsView.as_view()),
    
    #orders
    path('orders/', views.OrderListView.as_view()),
    path('user-orders/', views.UserOrderListView.as_view())
]