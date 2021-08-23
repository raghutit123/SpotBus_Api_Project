from rest_framework import serializers
from .models import School, Route


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('School_id','School_name', 'School_address', 'School_location')


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('__all__')
