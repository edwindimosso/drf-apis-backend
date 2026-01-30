from django.shortcuts import get_object_or_404
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer,OrderItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def productView(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    # Add safe=False here
    return Response(serializer.data)

@api_view(['GET'])
def productDetails(request, pk):
    product = get_object_or_404(Product, pk =pk)
    serializer= ProductSerializer(product)
    return Response(serializer.data)
    
@api_view(['GET'])
def orderView(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)