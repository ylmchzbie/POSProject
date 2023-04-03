from django.contrib.auth.models import User, Group
from JohnCarAirCo.models import (
  AirconType,
  ProductUnit,
  CustomerDetails,
  TechnicianDetails,
  ServiceType,
  SalesOrder,
  SalesOrderEntry,
  ServiceOrder,
  ServiceOrderEntry,
  SalesOrderPayment,
  ServiceOrderPayment,
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

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class ProductUnitSerializer(serializers.ModelSerializer):

  unit_type = serializers.StringRelatedField(many=False)
  unit_type_id = serializers.PrimaryKeyRelatedField(
    queryset=AirconType.objects.all(),
    source='unit_type',
  )

  class Meta:
    model = ProductUnit
    fields = [
      'id',
      'unit_name',
      'unit_price',
      'unit_stock',
      'unit_type',
      'unit_type_id'
    ]

class CustomerDetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomerDetails
    fields = [
      'id',
      'customer_name',
      'customer_contact',
      'customer_email',
      'customer_address'
    ]

class TechnicianDetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TechnicianDetails
    fields = [
      'id',
      'tech_name',
      'tech_phone',
      'tech_email',
      'tech_sched'
    ]

class ServiceTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ServiceType
    fields = [
      'service_name',
      'service_cost'
    ]

class AirconTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = AirconType
    fields = [
      'type_name',
    ]

class SalesOrderEntrySerializer(serializers.ModelSerializer):
  product = serializers.StringRelatedField(many=False)
  product_id = serializers.PrimaryKeyRelatedField(
    queryset=ProductUnit.objects.all(),
    source='product',
  )

  order = serializers.StringRelatedField(many=False)
  order_id = serializers.PrimaryKeyRelatedField(
    queryset=SalesOrder.objects.all(),
    source='order',
  )

  entry_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

  class Meta:
    model = SalesOrderEntry
    fields = [
      'id',
      'product',
      'product_id',
      'order',
      'order_id',
      'quantity',
      'entry_price'
    ]

  # add price to sales order total price
  def create(self, validated_data):
    order = validated_data['order']
    validated_data['entry_price'] = validated_data['product'].unit_price * validated_data['quantity']
    order.total_price += validated_data['entry_price']
    order.save()
    
    return SalesOrderEntry.objects.create(**validated_data)

  def update(self, instance, validated_data):
    order = validated_data['order']
    order.total_price -= instance.product.unit_price * instance.quantity
    
    validated_data['entry_price'] = validated_data['product'].unit_price * validated_data['quantity']
    order.total_price += validated_data['entry_price']
    order.save()

    instance.product = validated_data.get('product', instance.product)
    instance.quantity = validated_data.get('quantity', instance.quantity)
    instance.save()
    return instance


class SalesOrderSerializer(serializers.ModelSerializer):
  customer = serializers.StringRelatedField(many=False)
  customer_id = serializers.PrimaryKeyRelatedField(
    queryset=CustomerDetails.objects.all(),
    source='customer',
  )

  entries = SalesOrderEntrySerializer(many=True, read_only=True)

  total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

  class Meta:
    model = SalesOrder
    fields = [
      'id',
      'customer',
      'customer_id',
      'date_ordered',
      'total_price',
      'entries',
      'status',
      'total_price'
    ]

class ServiceTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ServiceType
    fields = [
      'id',
      'service_name',
      'service_cost'
    ]

class ServiceOrderEntrySerializer(serializers.ModelSerializer):
  service = serializers.StringRelatedField(many=False)
  service_id = serializers.PrimaryKeyRelatedField(
    queryset=ServiceType.objects.all(),
    source='service',
  )

  order = serializers.StringRelatedField(many=False)
  order_id = serializers.PrimaryKeyRelatedField(
    queryset=ServiceOrder.objects.all(),
    source='order',
  )

  entry_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

  class Meta:
    model = ServiceOrderEntry
    fields = [
      'id',
      'service',
      'service_id',
      'order',
      'order_id',
      'quantity',
      'entry_price',
    ]

  # add price to sales order total price
  def create(self, validated_data):
    order = validated_data['order']
    
    validated_data['entry_price'] = validated_data['service'].service_cost * validated_data['quantity']
    order.total_price += validated_data['entry_price']
    order.save()
    return ServiceOrderEntry.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    order = validated_data['order']
    order.total_price -= instance.service.service_cost * instance.quantity

    validated_data['entry_price'] = validated_data['service'].service_cost * validated_data['quantity']
    order.total_price += validated_data['entry_price']
    order.save()

    instance.service = validated_data.get('service', instance.service)
    instance.quantity = validated_data.get('quantity', instance.quantity)
    instance.save()
    return instance

class ServiceOrderSerializer(serializers.ModelSerializer):
  customer = serializers.StringRelatedField(many=False)
  customer_id = serializers.PrimaryKeyRelatedField(
    queryset=CustomerDetails.objects.all(),
    source='customer',
  )

  technician = serializers.StringRelatedField(many=False)
  technician_id = serializers.PrimaryKeyRelatedField(
    queryset=TechnicianDetails.objects.all(),
    source='technician',
  )

  entries = ServiceOrderEntrySerializer(many=True, read_only=True)

  service_date = serializers.DateField(format="%Y-%m-%d")

  total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

  class Meta:
    model = ServiceOrder
    fields = [
      'id',
      'customer',
      'customer_id',
      'date_ordered',
      'entries',
      'status',
      'technician',
      'technician_id',
      'service_date',
      'total_price',
    ]

class SalesOrderPaymentSerializer(serializers.ModelSerializer):
  order = serializers.StringRelatedField(many=False)
  order_id = serializers.PrimaryKeyRelatedField(
    queryset=SalesOrder.objects.all(),
    source='order',
  )

  class Meta:
    model = SalesOrderPayment
    fields = [
      'id',
      'order',
      'order_id',
      'amount_paid',
      'date_paid',
      'cc_number',
      'cc_name',
      'cc_expiry',
      'cc_cvv',
    ]

class ServiceOrderPaymentSerializer(serializers.ModelSerializer):
  order = serializers.StringRelatedField(many=False)
  order_id = serializers.PrimaryKeyRelatedField(
    queryset=ServiceOrder.objects.all(),
    source='order',
  )

  class Meta:
    model = ServiceOrderPayment
    fields = [
      'id',
      'order',
      'order_id',
      'amount_paid',
      'date_paid',
      'cc_number',
      'cc_name',
      'cc_expiry',
      'cc_cvv',
    ]