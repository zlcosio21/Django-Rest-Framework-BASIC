from rest_framework import serializers
from .models import Programmer, Product

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"