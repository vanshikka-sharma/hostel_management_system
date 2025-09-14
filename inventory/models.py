from django.db import models

class Item(models.Model):
    # No custom save method needed
    # No custom save method needed
    # No custom save method needed
    CATEGORY_CHOICES = [
        ('electric','Electrical'),
        ('furniture','Furniture'),
        ('Mess','Mess'),
        ('medical','Medical'),
        ('misc','Miscellaneous'),
    ]
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='misc')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    purchase_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def total_value(self):
        return self.price * self.quantity

    # No custom save method needed

    def __str__(self):
        return f"{self.name} ({self.category})"

class UsageRecord(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='usages')
    used_quantity = models.PositiveIntegerField()
    used_on = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Subtract used_quantity from item.quantity when usage is recorded
        if not self.pk:
            if self.used_quantity > self.item.quantity:
                raise ValueError("Used quantity cannot be greater than available quantity.")
            self.item.quantity -= self.used_quantity
            self.item.save()
        super().save(*args, **kwargs)

