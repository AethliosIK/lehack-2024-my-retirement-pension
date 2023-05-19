from rest_framework import serializers

from .models import Retirement

class RetirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retirement
        fields = ["uuid", "retirement"]
