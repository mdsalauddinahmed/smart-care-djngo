from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters,pagination

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .import models
from .import serializer

class SpecializationVewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializer.Specializationserializer

class DesignationVewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializer.Designationserializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor=doctor_id)
        return query_set

class AvailaleTimeVewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailaleTime.objects.all()
    serializer_class = serializer.AvailaleTimeserializer
    filter_backends=[AvailableTimeForSpecificDoctor]
class DoctorPagination(pagination.PageNumberPagination):
    page_size=1
    page_size_query_param=page_size
    max_page_size = 100


class  DoctorVewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializer.Doctorserializer
    pagination_class=DoctorPagination

class ReviewVewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializer.Reviewserializer