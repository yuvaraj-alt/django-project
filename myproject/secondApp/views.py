from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import  StudentModel


# Create your views here.

# @api_view(["GET","POST"])
# def studentView(request):
#     if request.method == "GET":
#         student = StudentModel.objects.all()
#         serializer = StudentSerializer(student,many=True)
#         return Response(serializer.data, status= status.HTTP_200_OK)
#     elif request.method == "POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(["GET", "PUT", "DELETE"])
# def studentView(request, pk):
#     try:
#         student = StudentModel.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = StudentSerializer(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "PUT":
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class studentApiView(APIView):
    def get(self,request):
        student = StudentModel.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

class studentSuperView(APIView):
    def get_solutions(self,pk):
        try:
          return StudentModel.objects.get(pk=pk)
        except StudentModel.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        student = self.get_solutions(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,pk):
        student = self.get_solutions(pk)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student = self.get_solutions(pk)
        student.delete()
        return Response(status= status.HTTP_410_GONE)

