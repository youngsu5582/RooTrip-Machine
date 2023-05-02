from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from .models import Sync

@api_view(['GET'])
def connectAPI(request):
    return Response(True)


@api_view(['GET'])
def connectSQL(request):
    sync = Sync
    temp = sync.objects.all().first()
    return Response(True)
