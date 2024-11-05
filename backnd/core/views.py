from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .serializers.retailer_serializers import FreshProduceRetailerSerializer
from .serializers.supplier_serializers import SupplierSerializer
from .models import (
    FreshProduceRetailer,
    Supplier,
    ProduceCategory,
    FreshProduce,
    Order,
    OrderItem,
    Delivery,
    QualityCheck,
    StorageOwner,
    StorageFacility,
    Product,
    StorageBooking,
    Payment,
    Review
)
from .forms import (
    FreshProduceRetailerForm,
    SupplierForm,
    ProduceCategoryForm,
    FreshProduceForm,
    OrderForm,
    OrderItemForm,
    DeliveryForm,
    QualityCheckForm,
    StorageOwnerForm,
    StorageFacilityForm,
    ProductForm,
    StorageBookingForm,
    PaymentForm,
    ReviewForm
)

# Retailer Views
@login_required
def retailer_list(request):
    retailers = FreshProduceRetailer.objects.all()
    return render(request, 'retailers/retailer_list.html', {'retailers': retailers})

@login_required
def retailer_detail(request, retailer_id):
    retailer = get_object_or_404(FreshProduceRetailer, id=retailer_id)
    return render(request, 'retailers/retailer_detail.html', {'retailer': retailer})

@login_required
def retailer_create(request):
    if request.method == 'POST':
        form = FreshProduceRetailerForm(request.POST)
        if form.is_valid():
            retailer = form.save(commit=False)
            retailer.user = request.user
            retailer.save()
            return redirect('retailer_detail', retailer_id=retailer.id)
    else:
        form = FreshProduceRetailerForm()
    return render(request, 'retailers/retailer_form.html', {'form': form})

@login_required
def retailer_update(request, retailer_id):
    retailer = get_object_or_404(FreshProduceRetailer, id=retailer_id)
    if request.method == 'POST':
        form = FreshProduceRetailerForm(request.POST, instance=retailer)
        if form.is_valid():
            form.save()
            return redirect('retailer_detail', retailer_id=retailer.id)
    else:
        form = FreshProduceRetailerForm(instance=retailer)
    return render(request, 'retailers/retailer_form.html', {'form': form})

@login_required
def retailer_delete(request, retailer_id):
    retailer = get_object_or_404(FreshProduceRetailer, id=retailer_id)
    if request.method == 'POST':
        retailer.delete()
        return redirect('retailer_list')
    return render(request, 'retailers/retailer_confirm_delete.html', {'retailer': retailer})

# Supplier Views
@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

@login_required
def supplier_detail(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    return render(request, 'suppliers/supplier_detail.html', {'supplier': supplier})

@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'suppliers/supplier_form.html', {'form': form})

@login_required
def supplier_update(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_detail', supplier_id=supplier.id)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'suppliers/supplier_form.html', {'form': form})

@login_required
def supplier_delete(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_confirm_delete.html', {'supplier': supplier})

# Produce Views
@login_required
def produce_list(request):
    produces = FreshProduce.objects.all()
    return render(request, 'produces/produce_list.html', {'produces': produces})

@login_required
def produce_detail(request, produce_id):
    produce = get_object_or_404(FreshProduce, id=produce_id)
    return render(request, 'produces/produce_detail.html', {'produce': produce})
