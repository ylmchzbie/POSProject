from django.db import models

# Create your models here.

class ProductUnit(models.Model):
    unitName = models.CharField(max_length=255, default='aircon')
    unitPrice = models.DecimalField(max_digits=12, decimal_places=2)
    #unitQuantity is stock
    unitQuantity = models.IntegerField()
    airconType = [
        ('Split Type', 'Split Type'),
        ('Window Air Conditioner', 'Window Air Conditioner'),
        ('N/A', 'N/A'),
    ]
    unitType = models.CharField(max_length=50, null=True, choices=airconType)

    def __str__(self):
        return self.unitName

class CustomerDetails(models.Model):
    customerName = models.CharField(max_length=255)
    customerContact = models.CharField(max_length=12)
    customerEmail = models.CharField(max_length=255)
    customerAddress = models.CharField(max_length=255)

    def __str__(self):
        return self.customerName

class TechnicianDetails(models.Model):
    techName = models.CharField(max_length=255)
    techPhone = models.CharField(max_length=12)
    techEmail = models.CharField(max_length=255)
    techSched = models.CharField(max_length=255)

    def __str__(self):
        return self.techName

class SupplierDetails(models.Model):
    suppName = models.CharField(max_length=255)
    suppPhone = models.CharField(max_length=12)
    suppEmail = models.CharField(max_length=255)
    suppAddress = models.CharField(max_length=255)

    def __str__(self):
        return self.suppName

class ServiceType(models.Model):
    servicesOffered = [
        ('Cars', 'Cars'),
        ('House', 'House'),
        ('Office', 'Office'),
        ('N/A', 'N/A'),
    ]
    serviceChoice = models.CharField(max_length=50, null=False, primary_key=True, choices=servicesOffered, default='N/A')
    estimatedCost = models.DecimalField(max_digits=12, decimal_places=2)

class SalesOrder(models.Model):
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    dateOrdered = models.DateField(auto_now_add=True)
    totalPrice = models.DecimalField(max_digits=12, decimal_places=2)
    products = models.ManyToManyField(ProductUnit, through='OrderItem')

    def __str__(self):
        return f"Order #{self.id} - {self.customer}"

class OrderItem(models.Model):
    product = models.ForeignKey(ProductUnit, on_delete=models.CASCADE)
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.unitName} in Order {self.order.id}'

class ServiceOrder(models.Model):
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    dateOrdered = models.DateField(auto_now_add=True)
    service = models.ForeignKey(ServiceType,on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.id} - {self.customer}"

class PurchaseOrder(models.Model):
    orderDate = models.DateField(auto_now_add=True)
    supplierName = models.ForeignKey(SupplierDetails, on_delete=models.CASCADE)
    customerName = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    deliveryDate = models.DateField()
    itemDesc = models.CharField(max_length=255)
    itemQuantity = models.PositiveIntegerField()
    itemCost = models.DecimalField(max_digits=12, decimal_places=2)