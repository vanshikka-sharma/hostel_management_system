from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    purchase_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.quantity} available)"

    def total_value(self):
        return self.price * self.quantity


class UsageRecord(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name="usage_records")
    used_quantity = models.PositiveIntegerField()
    used_on = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # reduce inventory quantity when usage is recorded
        if self.pk is None:  # only reduce on new record
            if self.item.quantity >= self.used_quantity:
                self.item.quantity -= self.used_quantity
                self.item.save()
            else:
                raise ValueError("Not enough stock available!")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Used {self.used_quantity} of {self.item.name} on {self.used_on}"

