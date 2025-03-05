from django.urls import path
from .views import ReservationListCreateView, ReservationDetailView, ReservationByUserView

urlpatterns = [
    path('', ReservationListCreateView.as_view(), name='reservation-list'),
    path('<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path('user/<int:user_id>/', ReservationByUserView.as_view(), name='reservation-by-user'),
]
