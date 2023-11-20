from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.cdr.models import CDR
from api.cdr.serializers import CdrSerializer
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CdrAPI(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CdrSerializer

    def post(self, request):
        serializer = CdrSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        called_number = request.data.get("called_number")
        calling_number = request.data.get("calling_number")
        call_start_time = request.data.get("call_start_time")
        call_end_time = request.data.get("call_end_time")
        status = request.data.get("status")
        call_type = request.data.get("call_type")
        call_duration = (datetime.fromisoformat(call_end_time.replace(
            'Z', '+00:00'))-datetime.fromisoformat(call_start_time.replace('Z', '+00:00'))).total_seconds()
        CDR.objects.create(called_number=called_number, calling_number=calling_number, call_start_time=call_start_time,
                           call_end_time=call_end_time, status=status, call_type=call_type, call_duration=call_duration)
        return Response(serializer.data)


    def get(self, request, *args, **kwargs):
        cdrs = CDR.objects.all()
        date = request.query_params.get('created_at')
        phone_number = request.query_params.get('phone_number')
        status = request.query_params.get('status')
        if date:
            cdrs = cdrs.filter(call_start_time=date)
        if phone_number:
            cdrs = cdrs.filter(calling_number=phone_number)
        if status:
            cdrs = cdrs.filter(status=status)
        serializer = CdrSerializer(cdrs, many=True)

        return Response(serializer.data)


class CdrDetailAPI(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CDR.objects.all()
    serializer_class = CdrSerializer
