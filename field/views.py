from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Job, Note, Image, Cost, Field
from .serializers import (
    JobSerializer,
    NoteSerializer,
    ImageSerializer,
    CostSerializer,
    FieldSerializer,
)
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# TODO create get user data api view


class CostListCreate(generics.ListCreateAPIView):
    serializer_class = CostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cost.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # assign user automatically


class CostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure user can only access their own notes
        return Cost.objects.filter(user=self.request.user)


class FieldListCreate(generics.ListCreateAPIView):
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Field.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # assign user automatically


class FieldDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure user can only access their own notes
        return Field.objects.filter(user=self.request.user)


class ImageListCreate(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # assign user automatically


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure user can only access their own notes
        return Image.objects.filter(user=self.request.user)


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # assign user automatically


class NoteDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure user can only access their own notes
        return Note.objects.filter(user=self.request.user)


class JobListCreate(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # assign user automatically


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure user can only access their own notes
        return Job.objects.filter(user=self.request.user)
