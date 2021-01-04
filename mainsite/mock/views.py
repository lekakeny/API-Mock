from rest_framework import viewsets
from .serializers import CustomizedSerializer
from .models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()[:50]
    serializer_class = CustomizedSerializer


