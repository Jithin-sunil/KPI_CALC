from rest_framework import serializers
from integrations.models import KPI

class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['metric_name', 'value', 'date_calculated', 'period']