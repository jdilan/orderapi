from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    price = serializers.CharField(max_length=10)

class OrderSerializer(serializers.Serializer):
    order_id = serializers.CharField(max_length=100)
    customer_id = serializers.CharField(max_length=100)
    order_date = serializers.CharField(max_length=10)
    shipped_date = serializers.CharField(max_length=10)
    status = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    items = ItemSerializer(many=True)  # 'many=True' allows a list of items

    # def validate_items(self, value):
    #     if not value:
    #         raise serializers.ValidationError("Order must contain at least one item.")
    #     return value
    