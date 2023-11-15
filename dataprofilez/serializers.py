from rest_framework import serializers
from dataprofilez.models import Sample

class SampleSerializer(serializers.Serializer):
    # model = Sample
    # fields = ('S_No','PId','PName','City','Hospital','Gender','BMI','DOB','Hieght','Weight','Diabetes')
    file = serializers.FileField()
