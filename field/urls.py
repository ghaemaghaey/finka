from django.urls import path
from .views import (
    JobListCreate,
    JobDetail,
    NoteListCreate,
    NoteDetails,
    ImageListCreate,
    ImageDetail,
    CostListCreate,
    CostDetail,
    FieldListCreate,
    FieldDetail,
)


def register_crud_urls(prefix, list_view, detail_view):
    return [
        path(f"{prefix}/", list_view.as_view(), name=f"{prefix}-list-create"),
        path(f"{prefix}/<int:pk>/", detail_view.as_view(), name=f"{prefix}-detail"),
    ]


urlpatterns = []

urlpatterns += register_crud_urls("jobs", JobListCreate, JobDetail)
urlpatterns += register_crud_urls("notes", NoteListCreate, NoteDetails)
urlpatterns += register_crud_urls("images", ImageListCreate, ImageDetail)
urlpatterns += register_crud_urls("costs", CostListCreate, CostDetail)
urlpatterns += register_crud_urls("fields", FieldListCreate, FieldDetail)


# urlpatterns = [
#     path("jobs/", JobListCreate.as_view(), name="job-createlist"),
#     path("jobs/<int:pk>/", JobDetail.as_view(), name="job-detail"),
#     path("notes/", NoteListCreate.as_view(), name="note-createlist"),
#     path("notes/<int:pk>/", NoteDetails.as_view(), name="note-detail"),
#     path("images/", ImageListCreate.as_view(), name="image-createlist"),
#     path("images/<int:pk>/", ImageDetail.as_view(), name="image-detail"),
# ]
