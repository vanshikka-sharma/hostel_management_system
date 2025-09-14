# staff/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from .models import StaffMember, Shift, ShiftAssignment, SalaryRecord
from .forms import StaffMemberForm, ShiftForm, ShiftAssignmentForm, SalaryRecordForm
from datetime import date

# Base: list all staff and quick actions
def base(request):
    q = request.GET.get('q','').strip()
    staff_type = request.GET.get('type','')
    staff_qs = StaffMember.objects.all()
    if q:
        staff_qs = staff_qs.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(phone__icontains=q))
    if staff_type:
        staff_qs = staff_qs.filter(staff_type=staff_type)
    context = {
        'staff_list': staff_qs,
        'types': StaffMember.STAFF_TYPE_CHOICES,
        'query': q,
        'selected_type': staff_type,
    }
    return render(request, 'staff/templates/base.html', context)

# Show shifts: by date, grouped by shift
def shift_overview(request):
    # default date today
    date_str = request.GET.get('date')
    if date_str:
        try:
            selected_date = date.fromisoformat(date_str)
        except Exception:
            selected_date = date.today()
    else:
        selected_date = date.today()

    assignments = ShiftAssignment.objects.filter(date=selected_date).select_related('shift','staff').order_by('shift__start_time','staff__first_name')
    shifts = Shift.objects.all().order_by('start_time')
    # build mapping shift -> assigned staff list
    shift_map = {s: [] for s in shifts}
    for a in assignments:
        shift_map.setdefault(a.shift, []).append(a)
    context = {
        'selected_date': selected_date,
        'shift_map': shift_map,
    }
    return render(request, 'staff/templates/shifts.html', context)

# Add/manage shifts page (create shift templates, assign staff)
def manage_shifts(request):
    # create new shift
    if request.method == 'POST' and 'create_shift' in request.POST:
        shift_form = ShiftForm(request.POST)
        if shift_form.is_valid():
            shift_form.save()
            messages.success(request, "Shift created.")
            return redirect('templates/staff:add')
    else:
        shift_form = ShiftForm()

    # assign staff to shift
    if request.method == 'POST' and 'assign_shift' in request.POST:
        assign_form = ShiftAssignmentForm(request.POST)
        if assign_form.is_valid():
            try:
                assign_form.save()
                messages.success(request, "Shift assigned.")
                return redirect('templates/staff:add')
            except Exception as e:
                messages.error(request, f"Could not assign: {e}")
    else:
        assign_form = ShiftAssignmentForm(initial={'date': date.today()})

    # show upcoming assignments
    upcoming = ShiftAssignment.objects.filter(date__gte=date.today()).order_by('date','shift__start_time')[:80]

    context = {
        'shift_form': shift_form,
        'assign_form': assign_form,
        'upcoming': upcoming,
    }
    return render(request, 'staff/templates/manage_shifts.html', context)

# Salary listing and management
def salary_overview(request):
    # filters
    year = request.GET.get('year')
    month = request.GET.get('month')
    qs = SalaryRecord.objects.select_related('staff').all()
    if year and year.isdigit():
        qs = qs.filter(year=int(year))
    if month and month.isdigit():
        qs = qs.filter(month=int(month))

    if request.method == 'POST' and 'create_salary' in request.POST:
        form = SalaryRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salary record created/updated.')
            return redirect(reverse('staff:salary'))
    else:
        form = SalaryRecordForm()

    context = {
        'salary_list': qs.order_by('-year','-month'),
        'form': form,
    }
    return render(request, 'staff/templates/salary.html', context)

# small helpers to add/edit staff (optional)
def staff_create(request):
    if request.method == 'POST':
        form = StaffMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff member added.")
            return redirect('templates/staff:base')
    else:
        form = StaffMemberForm()
    return render(request, 'staff/templates/staff_form.html', {'form': form})

def staff_edit(request, pk):
    obj = get_object_or_404(StaffMember, pk=pk)
    if request.method == 'POST':
        form = StaffMemberForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff updated.")
            return redirect('templates/staff:base')
    else:
        form = StaffMemberForm(instance=obj)
    return render(request, 'staff/templates/staff_form.html', {'form': form, 'obj': obj})


