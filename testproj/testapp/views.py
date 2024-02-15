from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
import boto3

def lambda_handler(data22):
    
    s3_client = boto3.client('s3')
    
    bucket = "zappa8368420316"
    key = "temp.txt"
    datainput = data22
    
    filepath = "/tmp/temp.txt" 
    
    # s3_client.download_file(bucket, key, filepath)
    
    with open(filepath, "a") as f:
        f.write("\n" + datainput)
        f.close()
    
    s3_client.upload_file(filepath, bucket, "temp.txt")
    
    return {
        'statusCode': 200,
        'body': json.dumps("File updated successfully.")
    }


class Dropdown1InfoGetApi(APIView):

    def get(self, request):

        data_to_write = '\n'+str(datetime.datetime.now())+' - Temporary data for Dropdown1InfoGetApi.'
        


        a= lambda_handler(data_to_write)
        rr = {
            "id": 1,
            "name": "Val1",
            "shortName": "V1",
            "lamba":a
        }
        return Response([rr], status=200)

    def post(self, request):
        pass

class Dropdown2InfoGetApi(APIView):

    def get(self,request):
        # pass
        # d=Dropdown2.objects.filter().order_by("id")
        # biS=Dropdown2Serializer001(d,many=True)
        # resultMain=biS.data
        rr=    {
        "id": 1,
        "name": "Val1",
        "shortName": "V1"
        }        
        return Response([rr], status=200)
    
    def post(self,request):
        pass

class Dropdown3InfoGetApi(APIView):

    def get(self,request):
        # pass
        # d=Dropdown3.objects.filter().order_by("id")
        # biS=Dropdown3Serializer001(d,many=True)
        # resultMain=biS.data
        rr=    {
        "id": 1,
        "name": "Val1",
        "shortName": "V1"
        }
        return Response([rr], status=200)
    
    def post(self,request):
        pass    
# Create your views here.
# def write_to_temp_file(data):
#     tmp_file_path = 'tmpfile.txt'
#     with open(tmp_file_path, 'a') as file:
#         file.write(data)
#         print("lllllll", data)
#     print(tmp_file_path)
#     return tmp_file_path

# def read_from_temp_file(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#     return content

# def upload_to_s3(local_file_path, bucket_name, s3_key):
#     s3 = boto3.client('s3')
#     s3.upload_file(local_file_path, bucket_name, s3_key)    
