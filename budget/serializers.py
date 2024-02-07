from .models import Budget, Marriage, Vendor
from rest_framework import serializers


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "name", "price"]


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ["id", "vendors", "marriage"]


class MarriageSerializer(serializers.ModelSerializer):
    budget = BudgetSerializer()

    class Meta:
        model = Marriage
        fields = ["id", "codename", "date", "budget"]
