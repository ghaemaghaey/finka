from django.urls import path
from .views import JobListView

urlpatterns = [
    path("jobs/v1/", JobListView.as_view()),
]
