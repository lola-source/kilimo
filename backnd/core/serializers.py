from rest_framework import serializers
from .models import (
    FreshProduceRetailer,
    Supplier,
    ProduceCategory,
    FreshProduce,
    Order,
    OrderItem,
    Delivery,
    QualityCheck,
    StorageOwner,
    StorageFacility,
    Product,
    StorageBooking,
    Payment,
    Review
)

class FreshProduceRetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreshProduceRetailer
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProduceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduceCategory
        fields = '__all__'

class FreshProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreshProduce
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class QualityCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityCheck
        fields = '__all__'

class StorageOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageOwner
        fields = '__all__'

class StorageFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageFacility
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StorageBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageBooking
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'