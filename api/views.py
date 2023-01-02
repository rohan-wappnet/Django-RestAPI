from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets, status
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many = True, context = {'request' : request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response({
                'status': False,
                'message' : 'Company might Not exist!! Error',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer