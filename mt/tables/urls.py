from django.urls import path
from .views import TableListCreateView, TableAvailableView

urlpatterns = [
    path('', TableListCreateView.as_view(), name='table-list'),
    path('available/', TableAvailableView.as_view(), name='table-available'),
]
