from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
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
from JohnCarAirCo.serializers import (
    UserSerializer,
    RegisterSerializer,
    GroupSerializer,
    ProductUnitSerializer,
    CustomerDetailsSerializer,
    TechnicianDetailsSerializer,
    SupplierDetailsSerializer,
    ServiceTypeSerializer,
    SalesOrderSerializer,
    OrderItemSerializer,
    ServiceOrderSerializer,
    PurchaseOrderSerializer
)
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics

class UserDetailAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductUnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ProductUnit.objects.all()
    serializer_class = ProductUnitSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomerDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CustomerDetails.objects.all()
    serializer_class = CustomerDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

class TechnicianDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TechnicianDetails.objects.all()
    serializer_class = TechnicianDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

class SupplierDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SupplierDetails.objects.all()
    serializer_class = SupplierDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

class ServiceTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class SalesOrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class ServiceOrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]