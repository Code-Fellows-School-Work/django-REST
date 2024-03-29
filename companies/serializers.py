from rest_framework import serializers
from .models import Companie

class CompanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companie
        fields = (
            "id",
            "owner",
            "name",
            "description",
            "created_on"
        )