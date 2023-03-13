from django.db import models

# Create your models here.

class ProductUnit(models.Model):
    airconType = [
        ('Split Type', 'Split Type'),
        ('Window Air Conditioner', 'Window Air Conditioner'),
        ('N/A', 'N/A'),
    ]
    unitName = models.CharField(max_length=255, null=False, primary_key=True, choices=airconType, default='N/A')
    unitPrice = models.DecimalField(max_digits=12, decimal_places=2)
    #unitQuantity is stock
    unitQuantity = models.IntegerField()

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

    def __str__(self):
        return f"{self.serviceChoice} Service"

class SalesOrder(models.Model):
    statusChoices = [
        ('Active', 'Active'),
        ('Finished', 'Finished'),
        ('Cancelled', 'Cancelled')
    ]
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    dateOrdered = models.DateField(auto_now_add=True)
    product = models.ForeignKey(ProductUnit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    @property
    def totalPrice(self):
        return sum([item.product.unitPrice * item.quantity for item in self.products.all()])
    status = models.CharField(max_length=255, choices=statusChoices, default='Active')

    def __str__(self):
        return f"Order #{self.id} - {self.customer}"

class ServiceOrder(models.Model):
    statusChoices = [
        ('Active', 'Active'),
        ('Finished', 'Finished'),
        ('Cancelled', 'Cancelled')
    ]
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    technician = models.ForeignKey(TechnicianDetails, on_delete=models.CASCADE)
    dateOrdered = models.DateField(auto_now_add=True)
    service = models.ForeignKey(ServiceType,on_delete=models.CASCADE)
    serviceDate = models.DateField()
    status = models.CharField(max_length=255, choices=statusChoices, default='Active')

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