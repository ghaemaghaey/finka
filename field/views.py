from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Job
from .serializers import JobSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class JobListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_user = request.user
        jobs = Job.objects.filter(user=current_user)
        serilizer = JobSerializer(jobs, many=True)
        return Response(serilizer.data)
