from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializer

class ContactVewSet(viewsets.ModelViewSet):
    queryset = models.contactus.objects.all()
    serializer_class = serializer.contactserializer