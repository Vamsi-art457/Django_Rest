from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def get_students(request):
    students=Student.objects.all()
    serializer=StudentSerializer(
        students,
        many=True
    )
    return Response(serializer.data)

@api_view(['GET'])
def get_student(request,id):
    student=Student.objects.get(id=id)
    serializer=StudentSerializer(student)
    return Response(serializer.data)

@api_view(['POST'])
def add_student(request):
    serializer=StudentSerializer(
        data=request.data
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_student(request,id):
    student=Student.objects.get(id=id)
    serializer=StudentSerializer(
        student,
        data=request.data
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return Response({
        "message":"Deleted Succussfully"
    })
    



