from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date

# Custom validator for age
def validate_age(value):
    if value < 18:
        raise ValidationError("Patients must be older than 18 years.")

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[validate_age])
    sex = models.CharField(max_length=10)
    problem = models.TextField()
    nic = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    mfg_date = models.DateField()
    expiry_date = models.DateField()
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Transaction of {self.product.name} to {self.patient.name} on {self.date}"
