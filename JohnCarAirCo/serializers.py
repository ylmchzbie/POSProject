from django.contrib.auth.models import User, Group
from JohnCarAirCo.models import (
  ProductUnit,
  CustomerDetails,
  TechnicianDetails,
  SupplierDetails,
  ServiceType,
  SalesOrder,
  OrderItem,
  ServiceOrder,
  PurchaseOrder
)
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username"]

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }

  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError({"password": "Password fields didn't match."})
    return attrs

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class ProductUnitSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ProductUnit
    fields = [
      'unitName',
      'unitPrice',
      'unitQuantity',
      'airconType',
      'unitType'
    ]

class CustomerDetailsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = CustomerDetails
    fields = [
      'customerName',
      'customerContact',
      'customerEmail',
      'customerAddress'
    ]

class TechnicianDetailsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = TechnicianDetails
    fields = [
      'techName',
      'techPhone',
      'techEmail',
      'techSched'
    ]

class SupplierDetailsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = SupplierDetails
    fields = [
      'suppName',
      'suppPhone',
      'suppEmail',
      'suppAddress'
    ]

class ServiceTypeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ServiceType
    fields = [
      'servicesOffered',
      'serviceChoice',
      'estimatedCost'
    ]

class SalesOrderSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = SalesOrder
    fields = [
      'customer',
      'dateOrdered',
      'totalPrice',
      'products'
    ]

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = OrderItem
    fields = [
      'product',
      'order',
      'quantity'
    ]

class ServiceOrderSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ServiceOrder
    fields = [
      'customer',
      'dateOrdered',
      'service'
    ]

class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PurchaseOrder
    fields = [
      'orderDate',
      'supplierName',
      'customerName',
      'deliveryDate',
      'itemDesc',
      'itemQuantity',
      'itemCost'
    ]
