from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import School
from .serializers import SchoolSerializer


class SchoolList(generics.ListCreateAPIView):
	queryset = School.objects.all()[:20]
	serializer_class = SchoolSerializer
	# def get(self, request):
	# 	schools = School.objects.all()[:20]
	# 	data = SchoolSerializer(schools, many=True).data
	# 	return Response(data)

class SchoolDetail(generics.RetrieveDestroyAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

	# def get(self, request, pk):
	# 	school = get_object_or_404(School, pk=pk)
	# 	data = SchoolSerializer(school).data
	# 	return Response(data)