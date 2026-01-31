from django.db.models import Max
from django.shortcuts import get_object_or_404
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer,OrderItemSerializer, ProductInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer
    
class productDetailsView(generics.RetrieveAPIView):
   queryset = Product.objects.all()
   serializer_class= ProductSerializer

    
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product').all()
    serializer_class = OrderSerializer

@api_view(['GET'])
def productInfoView(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price' : products.aggregate(max_price= Max('price'))['max_price']})
    
    return Response(serializer.data)

