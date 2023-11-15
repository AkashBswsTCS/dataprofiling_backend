from django.urls import include,path
from dataprofilez.views import FileUploadView

app_name = "dataprofilez"
urlpatterns = [
    path('upload-csv/', FileUploadView.as_view(), name='file-upload'),
    ]