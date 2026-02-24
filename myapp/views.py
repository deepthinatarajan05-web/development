from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import student
from .serializers import StudentSerializer
@api_view(['GET','PUT','PATCH','DELETE'])
def students(request,id=None):
    if request.method=='GET' and id is None:
        stu=student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    

    if request.method=='GET' and id is not None:
        stu=student.objects.get(id=id)
        serializer=StudentSerializer(stu)
        return Response(serializer.data)

    if request.method=='PUT':
       stu=student.objects.get(id=id)
       serializer=StudentSerializer(stu,data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
       return Response(serializer.errors)
   

    if request.method=='PATCH':
        stu=student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data ,partial=True)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors)

    if request.method=='DELETE':
       stu=student.objects.get(id=id)
       stu.delete()
       return Response("success")