from django.shortcuts import render, redirect, get_object_or_404
from .models import InventoryItem, UsageRecord
from .forms import InventoryItemForm, UsageRecordForm


def item_list(request):
    items = InventoryItem.objects.all().order_by("category", "name")
    return render(request, "inventory/templates/item_list.html", {"items": items})


def add_item(request):
    if request.method == "POST":
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    else:
        form = InventoryItemForm()
    return render(request, "inventory/templates/item_form.html", {"form": form})


def record_usage(request):
    if request.method == "POST":
        form = UsageRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    else:
        form = UsageRecordForm()
    return render(request, "inventory/templates/usage_form.html", {"form": form})

