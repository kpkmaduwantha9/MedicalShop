from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient, Product, Transaction

from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')


# Patient CRUD Operations
@login_required
def list_patients(request):
    patients = Patient.objects.all()
    return render(request, 'list_patients.html', {'patients': patients})

@login_required
def add_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        sex = request.POST['sex']
        problem = request.POST['problem']
        nic = request.POST['nic']
        
        patient = Patient(name=name, age=age, sex=sex, problem=problem, nic=nic)
        patient.save()
        return redirect('list_patients')
    return render(request, 'add_patient.html')

@login_required
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.age = request.POST['age']
        patient.sex = request.POST['sex']
        patient.problem = request.POST['problem']
        patient.nic = request.POST['nic']
        patient.save()
        return redirect('list_patients')
    return render(request, 'edit_patient.html', {'patient': patient})

@login_required
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('list_patients')
    return render(request, 'confirm_delete.html', {'patient': patient})

# Product CRUD Operations
@login_required
def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        mrp = request.POST['mrp']
        mfg_date = request.POST['mfg_date']
        expiry_date = request.POST['expiry_date']
        stock_quantity = request.POST['stock_quantity']
        
        product = Product(name=name, mrp=mrp, mfg_date=mfg_date, expiry_date=expiry_date, stock_quantity=stock_quantity)
        product.save()
        return redirect('list_products')
    return render(request, 'add_product.html')

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.mrp = request.POST['mrp']
        product.mfg_date = request.POST['mfg_date']
        product.expiry_date = request.POST['expiry_date']
        product.stock_quantity = request.POST['stock_quantity']
        product.save()
        return redirect('list_products')
    return render(request, 'edit_product.html', {'product': product})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    return render(request, 'confirm_delete_product.html', {'product': product})

@login_required
def transaction_report(request):
    # Summarize transaction data
    transactions = Transaction.objects.all()
    total_sales = transactions.aggregate(Sum('quantity'))['quantity__sum'] or 0

    # Retrieve product details
    products = Product.objects.all()
    
    # Prepare context data for the template
    context = {
        'transactions': transactions,
        'total_sales': total_sales,
        'products': products,
    }
    
    return render(request, 'transaction_report.html', context)