from django.urls import path
from .views import send_data_to_kafka

urlpatterns = [
    # path('api/data/', send_data_to_kafka, name='send_data_to_kafka'),
    path('', send_data_to_kafka, name='send_data_to_kafka'),
]
