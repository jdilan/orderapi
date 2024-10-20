import json
from confluent_kafka import Producer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import OrderSerializer
from .kafka_utils import send_data

# class OrderView(APIView):
#    def post(self, request):
@api_view(['POST'])
def send_data_to_kafka(request):
    serializer = OrderSerializer(data=request.data)
    
    if serializer.is_valid():
        # Access the validated order data
        validated_data = serializer.validated_data
        
        # Convert the data to JSON string to push to Kafka
        # order_data_json = json.dumps(data)

        try:
            # Send the order data to Kafka (topic 'order-topic')
            send_data(settings.KAFKA_TOPIC, json.dumps(validated_data).encode("utf-8"))

        except Exception as e:
            return Response({'error': 'Failed to send data to Kafka', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(validated_data, status=status.HTTP_200_OK)
    
    # If data is invalid, return the error
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
