from rest_framework import serializers
from tours_api.models import Tour

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        # fields = ['name', 'age', 'image']
        fields = '__all__'
