from rest_framework import serializers
from .models import Api


class Details(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = "__all__"