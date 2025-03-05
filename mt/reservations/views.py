from rest_framework import generics, status
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationListCreateView(generics.ListCreateAPIView):
    """Создать бронь или получить список всех броней"""
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        customer_id = request.data.get("customer")
        table_id = request.data.get("table")
        date = request.data.get("date")

        # Проверяем, есть ли уже бронь на этот столик в этот день
        if Reservation.objects.filter(table_id=table_id, date=date).exists():
            return Response({"error": "Table is already reserved for this date."}, status=status.HTTP_400_BAD_REQUEST)

        # Проверяем, есть ли у пользователя бронь на этот день
        if Reservation.objects.filter(customer_id=customer_id, date=date).exists():
            return Response({"error": "Customer already has a reservation for this date."}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Получить, обновить или удалить конкретную бронь"""
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationByUserView(generics.ListAPIView):
    """Получить список всех броней конкретного пользователя"""
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Reservation.objects.filter(customer_id=user_id)
