from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.contrib.auth.models import User

class Dropdown1InfoGetApi(APIView):

    def get(self,request):
        pass
        d=Dropdown1.objects.filter().order_by("id")
        biS=Dropdown1Serializer001(d,many=True)
        resultMain=biS.data
        return Response(resultMain, status=200)
    
    def post(self,request):
        pass

class Dropdown2InfoGetApi(APIView):

    def get(self,request):
        pass
        d=Dropdown2.objects.filter().order_by("id")
        biS=Dropdown2Serializer001(d,many=True)
        resultMain=biS.data
        return Response(resultMain, status=200)
    
    def post(self,request):
        pass

class Dropdown3InfoGetApi(APIView):

    def get(self,request):
        pass
        d=Dropdown3.objects.filter().order_by("id")
        biS=Dropdown3Serializer001(d,many=True)
        resultMain=biS.data
        return Response(resultMain, status=200)
    
    def post(self,request):
        pass    
# Create your views here.
