from django.urls import path
from .views import customer_list, CustomerListCreateView, CustomerDetailView

urlpatterns = [
    # HTML-страница
    path('', customer_list, name='customer_list'),

    # API-эндпоинты
    path('api/', CustomerListCreateView.as_view(), name='customer_list_api'),
    path('api/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail_api'),
]
