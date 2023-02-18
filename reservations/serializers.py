from rest_framework.serializers import ModelSerializer

from .models import Reservation

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'first_name', 'last_name', 'email', 'age','city','state','zipcode','url','created_date','other' ]