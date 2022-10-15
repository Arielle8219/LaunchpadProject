from rest_framework import serializers
from .models import TreeLoss
# specifies which model we're working with, and what to convert to json

class TreeLossSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeLoss
        fields = ('title', 'description')