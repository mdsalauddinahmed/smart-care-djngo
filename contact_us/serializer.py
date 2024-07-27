from rest_framework import serializers
from .import models


class contactserializer(serializers.ModelSerializer):
    class Meta:
        model= models.contactus
        fields= '__all__'