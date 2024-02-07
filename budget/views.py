from rest_framework import viewsets
from .models import Vendor, Marriage, Budget
from .serializers import (
    VendorSerializer,
    MarriageSerializer,
    BudgetSerializer,
    AdminVendorSerializer,
)


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class MarriageViewSet(viewsets.ModelViewSet):
    queryset = Marriage.objects.all()
    serializer_class = MarriageSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = AdminVendorSerializer

    def get_serializer_class(self):
        if self.action in ("create", "destroy", "update"):
            return AdminVendorSerializer
        return VendorSerializer
