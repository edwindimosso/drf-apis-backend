from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price','stock')

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be gretarer than 0.")
        return value
    

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model= OrderItem
        fields = ('product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name= 'total')

    class Meta:
        model= Order
        fields = ('order_id','user', 'status', 'created_at', 'items', 'total_price')

    def total(self, obj):
        order_items = obj.items.all()
        return sum(order_item.subtotal for order_item in order_items)
