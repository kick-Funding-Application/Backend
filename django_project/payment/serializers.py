from rest_framework import serializers
from .models import Payment
from projects.models import Project
from django.utils import timezone 
from datetime import timedelta

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('input_amount', 'project', 'user', 'created_at',
                  'target_amount', 'current_amount')
        
class DonateToProject(serializers.ModelSerializer):
    donations = serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields = ('input_amount', 'project', 'user', 'created_at',
                  'target_amount', 'current_amount','donations')
    def get_donations(self, obj):
        start_date = timezone.now().date()
        end_date = start_date + timedelta(days=1)
        
        donation_list = Payment.objects.filter(
            created_at__range=(start_date, end_date)
        )
        serialized_donations = PaymentSerializer(donation_list, many=True).data
        return serialized_donations



class UpdateDonateProject(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('current_amount',)
