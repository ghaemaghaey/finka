from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class JobListView(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serilizer = JobSerializer(jobs, many=True)
        return Response(serilizer.data)
