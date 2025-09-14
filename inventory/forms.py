from django import forms
from .models import InventoryItem, UsageRecord


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ["name", "category", "price", "quantity", "purchase_date"]


class UsageRecordForm(forms.ModelForm):
    class Meta:
        model = UsageRecord
        fields = ["item", "used_quantity", "used_on", "notes"]
