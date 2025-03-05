from django.shortcuts import render
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer

# ✅ HTML-страница со списком клиентов
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customers/customer_list.html", {"customers": customers})

# ✅ API для списка клиентов (GET /customers/ и POST /customers/)
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# ✅ API для получения информации о клиенте (GET /customers/{id}/)
class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
