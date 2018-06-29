from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import School
from .serializers import SchoolSerializer


class SchoolList(generics.ListCreateAPIView):
	queryset = School.objects.all()[:20]
	serializer_class = SchoolSerializer
	
class SchoolDetail(generics.RetrieveDestroyAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

	