from django.shortcuts import render, redirect, get_object_or_404
from .models import MessMenu
from .forms import MessMenuForm
from inventory.models import Item

def mess_timetable(request):
    menu = MessMenu.objects.all().order_by("id")
    return render(request, "mess/templates/mess_timetable.html", {"menu": menu})

def add_menu(request, pk=None):
    if pk:  # Update
        menu_item = get_object_or_404(MessMenu, pk=pk)
    else:   # Add
        menu_item = None

    if request.method == "POST":
        form = MessMenuForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect("mess_timetable")
    else:
        form = MessMenuForm(instance=menu_item)

    return render(request, "mess/templates/add_menu.html", {"form": form})

def mess_inventory(request):
    items = Item.objects.filter(category='Mess')
    return render(request, "mess/templates/mess_inventory.html", {"items": items})
