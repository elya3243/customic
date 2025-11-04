from django.urls import path
from .views import MockupListAPIView, MockupCreateAPIView, MockupStatusAPIView

urlpatterns = [
    path('mockups/', MockupListAPIView.as_view(), name='list'),
    path('mockups/generate/', MockupCreateAPIView.as_view(), name='create'),
    path('tasks/<str:task_id>/', MockupStatusAPIView.as_view(), name='status'),
]
