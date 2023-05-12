from urllib import request
from rest_framework import serializers
from .models import Payment
from projects.models import Project


class DonateToProject(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('input_amount', 'project', 'user', 'created_at',
                  'target_amount', 'current_amount',)


class UpdateDonateProject(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('current_amount',)
