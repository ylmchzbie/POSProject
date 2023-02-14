from django.shortcuts import render
from django.contrib import messages
from .models import CustomerDetails

# Create your views here.

def customerDisplay(request):
    results = CustomerDetails.objects.all()

def newCustomer(request):
    if request.method=="POST":
        if request.POST.get('customerName') and request.POST.get('customerContact') and request.POST.get('customerEmail') and request.POST.get('customerAddress'):
            saveCustomer = CustomerDetails()
            saveCustomer.customerName=request.POST.get('customerName')
            saveCustomer.customerContact=request.POST.get('customerPhone')
            saveCustomer.customerEmail=request.POST.get('customerEmail')
            saveCustomer.customerAddress=request.POST.get('customerAddress')
            saveCustomer.save()
            messages.success(request, "Customer Record" + saveCustomer.customerName + "'s details is recorded!")
            return render(request,"createOrder.html")
        else:
            return render(request,"createOrder.html")

def createSalesOrder(request):
    if request.method=="POST":
        form = (request.POST)