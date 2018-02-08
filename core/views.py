from django.shortcuts import render
from .models import DataStore, Risk
import json
from django.http import JsonResponse
from .serializers import *


def index(request):
    return render(request, 'core/index.html')


def risk_list(request):
    risks = Risk.objects.all()
    sRisk = RiskSerializer(risks, many=True)
    return JsonResponse(sRisk.data, safe=False)


def risk_detail(request, pk):
    risk = Risk.objects.get(id=pk)
    sRisk = RiskSerializer(risk)
    return JsonResponse(sRisk.data, safe=False)
