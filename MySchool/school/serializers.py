"""
By: Bagiliko John
Year: 2018
""" 
from rest_framework import serializers
from .models import School
class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School
		fields = '__all__'
		