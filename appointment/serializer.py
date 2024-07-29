from rest_framework import serializers
from .import models


class Appointmentserializer(serializers.ModelSerializer):
    class Meta:
        model= models.Appointment
        fields= '__all__'