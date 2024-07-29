from rest_framework import serializers
from .import models


class Patientserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model= models.Patient
        fields= '__all__'