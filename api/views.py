from django.shortcuts import render
import requests
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .serializers import InventorySerializer
from .models import Inventory


# Create your views here.


def say_hello(request):
    return HttpResponse("Hello everybody")


def index(request):
    response = requests.get('http://127.0.0.1:8000/api/inventory/').json()
    return render(request, 'Index.html', {'response': response})


def success_test(request):
    return render(request, 'aview.html')


# class InventoryViewSet(viewsets.ModelViewSet):
#     queryset = Inventory.objects.all().order_by('name')
#     serializer_class = InventorySerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by('name')
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    # search_fields = ['name', 'description']
