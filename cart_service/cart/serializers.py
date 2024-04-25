from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product_id', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['created_at', 'total', 'user_id', 'cart_items']
        extra_kwargs = {
            'user_id': {'read_only': True}
        }

    def create(self, validated_data):
        cart_items_data = validated_data.pop('cart_items')
        cart = Cart.objects.create(**validated_data)
        sum = 0
        for item in cart_items_data:
            # //**validated_data unpack tất cả các cặp khóa-giá trị trong từ điển validated_data và truyền chúng như là các đối số được đặt tên vào phương thức create của đối tượng Cart.
            cart_item = CartItem.objects.create(cart=cart, **item)
            sum += cart_item.price * cart_item.quantity
        cart.total = sum
        cart.save()
        return cart