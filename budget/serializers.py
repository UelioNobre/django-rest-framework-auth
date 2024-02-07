from .models import Budget, Marriage, Vendor
from rest_framework import serializers


class VendorSerializer(serializers.HyperlinkedModelSerializer):
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

    def create(self, validated_data):
        budget_data = validated_data.pop("budget")
        budget_data["marriage"] = Marriage.objects.create(**validated_data)
        BudgetSerializer().create(validated_data=budget_data)
        return budget_data["marriage"]
