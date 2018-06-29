from rest_framework import serializers
from .models import School
class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School
		fields = '__all__'
		# fields = ('url', 'id', 'name', 'email', 'address_and_info', 'image', 'marked')