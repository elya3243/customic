from django.urls import path
from .views import MockupListView, MockupCreateView, MockupStatusAPIView


urlpatterns = [
    path('mockups/', MockupListView.as_view(), name='list'),
    path('mockups/generate/', MockupCreateView.as_view(), name='create'),
    path('tasks/<str:task_id>/', MockupStatusAPIView.as_view(), name='status'),
]