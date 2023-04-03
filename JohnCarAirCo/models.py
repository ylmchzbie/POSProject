from django.db import models

# Create your models here.

class AirconType(models.Model):
    type_name = models.CharField(max_length=255, null=False, primary_key=True)

    def __str__(self):
        return self.type_name

class ProductUnit(models.Model):
    unit_name = models.CharField(max_length=255, null=False)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    unit_type = models.ForeignKey(AirconType, on_delete=models.SET_NULL, null=True)
    unit_stock = models.IntegerField()

    def __str__(self):
        return self.unit_name

class CustomerDetails(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_contact = models.CharField(max_length=12)
    customer_email = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)

    def __str__(self):
        return self.customer_name

class TechnicianDetails(models.Model):
    tech_name = models.CharField(max_length=255)
    tech_phone = models.CharField(max_length=12)
    tech_email = models.CharField(max_length=255)
    tech_sched = models.CharField(max_length=255)

    def __str__(self):
        return self.tech_name

class ServiceType(models.Model):
    service_name = models.CharField(max_length=50, null=False)
    service_cost = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.service_name}"

class SalesOrderEntry(models.Model):
    order = models.ForeignKey('SalesOrder', on_delete=models.CASCADE, related_name='entries')
    product = models.ForeignKey(ProductUnit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    entry_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product} x{self.quantity}"

class SalesOrder(models.Model):
    status_choices = [
        ('Active', 'Active'),
        ('Finished', 'Finished'),
        ('Cancelled', 'Cancelled')
    ]
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    date_ordered = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    status = models.CharField(max_length=255, choices=status_choices, default='Active')

    def __str__(self):
        return f"Order #{self.id} - {self.customer}"

class ServiceOrderEntry(models.Model):
    order = models.ForeignKey('ServiceOrder', on_delete=models.CASCADE, related_name='entries')
    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    entry_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.service} x{self.quantity}"

class ServiceOrder(models.Model):
    status_choices = [
        ('Active', 'Active'),
        ('Finished', 'Finished'),
        ('Cancelled', 'Cancelled')
    ]
    customer = models.ForeignKey(CustomerDetails, on_delete=models.SET_NULL, null=True)
    technician = models.ForeignKey(TechnicianDetails, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    
    service_date = models.DateField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=255, choices=status_choices, default='Active')

    def __str__(self):
        return f"Order #{self.id} - {self.customer}"
    
class SalesOrderPayment(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)

    cc_number = models.CharField(max_length=16, null=True)
    cc_name = models.CharField(max_length=255, null=True)
    cc_expiry = models.CharField(max_length=5, null=True)
    cc_cvv = models.CharField(max_length=3, null=True)

    is_cash = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Sales Order #{self.order.id}"
    
class ServiceOrderPayment(models.Model):
    order = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)

    cc_number = models.CharField(max_length=16, null=True)
    cc_name = models.CharField(max_length=255, null=True)
    cc_expiry = models.CharField(max_length=5, null=True)
    cc_cvv = models.CharField(max_length=3, null=True)

    is_cash = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Service Order #{self.order.id}"