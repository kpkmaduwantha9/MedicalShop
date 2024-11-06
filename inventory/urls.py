from django.urls import path
from .views import (
    list_patients,
    add_patient,
    edit_patient,
    delete_patient,
    list_products,
    add_product,
    edit_product,
    delete_product,
    transaction_report,
)

urlpatterns = [
    path('patients/', list_patients, name='list_patients'),
    path('patients/add/', add_patient, name='add_patient'),
    path('patients/edit/<int:patient_id>/', edit_patient, name='edit_patient'),
    path('patients/delete/<int:patient_id>/', delete_patient, name='delete_patient'),
    path('products/', list_products, name='list_products'),
    path('products/add/', add_product, name='add_product'),
    path('products/edit/<int:product_id>/', edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', delete_product, name='delete_product'),
    path('report/', transaction_report, name='transaction_report'),
]
