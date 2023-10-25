from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *


# Create your views here.



@api_view(['GET', 'POST'])
def get_employee(request, format=None):
    """
    The function has get and post capabilities for the employee data

    :param request:
    :param format: the format=None is to add access to the employee.json
    :return: the needed employee data
    """
    if request.method == 'GET':
        output = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(output, many=True)
        return JsonResponse({"data": serializer.data})

    if request.method == 'POST':
        output = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_employee_details(request, id, format=None):
    """
     The function has get, put and delete capabilities for the individual employee data

    :param request:
    :param id: this is the employee id
    :param format: add access to the employee.json
    :return: the needed employee data
    """
    try:
        employee = EmployeeModel.objects.get(pk=id)
    except EmployeeModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

