from django.shortcuts import render
from openpyxl import load_workbook

from dataprofilez.serializers import SampleSerializer
from .models import Sample
from django.http import HttpResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from tablib import Dataset
from import_export.resources import ModelResource
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import openpyxl
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from import_export import resources
from django.core import serializers
from django.http import JsonResponse
from .forms import CSVUploadForm
import pandas
from django.http import JsonResponse
from rest_framework.views import APIView
from pandas_profiling import ProfileReport

import requests



class FileUploadView(APIView):
    serializer_class = SampleSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        # data = request.FILES
        # serializer = self.serializer_class(data=request.data)
        file_serializer = SampleSerializer(data=request.data)

        if file_serializer.is_valid():
            file_obj = file_serializer.validated_data['file']
            df = pandas.read_csv(file_obj)
            for index,row in df.iterrows():
                if Sample.objects.filter(PId=row['PId']).exists():
                    continue
                obj = Sample(
                    S_No = row['S.No'],
                    PId =  row['PId'],
                    PName = row['PName'],
                    City = row['City'],
                    Hospital_Name = row['Hospital Name'],
                    Gender = row['Gender'],
                    BMI = row['BMI'],
                    DOB = row['DOB'],
                    Hieght = row['Highet'],
                    Weight = row['Weight'],
                    Diabetic = row['Diabetic'],
                )
                obj.save()
            profile_result = ProfileReport(df,minimal=True)
            json_result = profile_result.to_json()
            return Response(json_result)
        
        else:
            return Response( file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)