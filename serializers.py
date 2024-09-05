from rest_framework import serializers
from .models import Transaction, SavingPlan, Budget

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'amount', 'category', 'date', 'transaction_type']

class SavingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingPlan
        fields = ['id', 'user', 'title', 'target_amount', 'saved_amount', 'monthly_saving', 'complete']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'category', 'budget_amount', 'remaining_amount']