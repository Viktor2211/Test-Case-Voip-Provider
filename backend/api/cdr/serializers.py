from rest_framework import serializers
from apps.cdr.models import CDR


class CdrSerializer(serializers.ModelSerializer):


    status = serializers.CharField(source='get_status_display')
    call_type = serializers.CharField(source='get_call_type_display')

    class Meta:
        model = CDR
        fields = ['id', 'called_number', 'calling_number', 'call_start_time', 'call_end_time', 'status', 'call_type', 'created_at', 'call_duration']