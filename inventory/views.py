from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, UsageRecord
from django.contrib import messages

CATEGORY_COLORS = {
    'bulb': 'bg-yellow-100 text-yellow-800',
    'fan': 'bg-blue-100 text-blue-800',
    'furniture': 'bg-green-100 text-green-800',
    'table_chair': 'bg-purple-100 text-purple-800',
    'kitchen': 'bg-pink-100 text-pink-800',
    'spoon': 'bg-orange-100 text-orange-800',
    'misc': 'bg-gray-100 text-gray-800',
}

def inventory_main(request):
    user = request.user
    if user.is_authenticated and getattr(user, 'role', None) == 'student':
        messages.info(request, 'Students cannot access inventory pages.')
        return redirect('home')
    items = Item.objects.all().order_by('-created_at')
    for item in items:
        item.color_class = CATEGORY_COLORS.get(item.category, 'bg-gray-100 text-gray-800')
        item.total_value = item.total_value()
    return render(request, 'inventory_main.html', {'items': items})

def inventory_add(request):
    user = request.user
    if user.is_authenticated and getattr(user, 'role', None) == 'student':
        messages.info(request, 'Students cannot access inventory pages.')
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        purchase_date = request.POST.get('purchase_date')
        if not (name and category and price and quantity and purchase_date):
            messages.error(request, "All fields are required.")
            return redirect('inventory_add')
        item = Item.objects.create(
            name=name,
            category=category,
            price=price,
            quantity=quantity,
            purchase_date=purchase_date
        )
        messages.success(request, "Item added successfully!")
        return redirect('inventory_main')
    return render(request, 'inventory_add.html')

def inventory_usage(request):
    user = request.user
    if user.is_authenticated and getattr(user, 'role', None) == 'student':
        messages.info(request, 'Students cannot access inventory pages.')
        return redirect('home')
    items = Item.objects.all()
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        used_quantity = int(request.POST.get('used_quantity'))
        used_on = request.POST.get('used_on')
        notes = request.POST.get('notes', '')
        item = get_object_or_404(Item, pk=item_id)
        if used_quantity > item.quantity:
            messages.error(request, "Used quantity cannot be greater than available quantity.")
            return redirect('inventory_usage')
        UsageRecord.objects.create(
            item=item,
            used_quantity=used_quantity,
            used_on=used_on,
            notes=notes
        )
        messages.success(request, "Usage recorded successfully!")
        return redirect('inventory_main')
    return render(request, 'inventory_usage.html', {'items': items})

