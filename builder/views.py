from msilib.schema import ListView
from celery.result import AsyncResult
from rest_framework import filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MockupSerializer
from .models import Mockup
from .tasks import mockup_builder


class MockupCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    model = Mockup
    serializer_class = MockupSerializer
    queryset = Mockup.objects.all()
    def post(self, request, *args, **kwargs):
        original = super().post(request, *args, **kwargs)
        task_id = mockup_builder.delay(original.data['id'])
        result = {'task_id':str(task_id), 'status':'PENDING', 'message':'ساخت تصویر آغاز شد.'}
        return Response(result)

class MockupListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Mockup.objects.all()
    model = Mockup
    serializer_class = MockupSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['text']
    def get_queryset(self):
        return Mockup.objects.filter()

class MockupStatusAPIView(APIView):
    def get(self, request, task_id):
        result = AsyncResult(task_id)
        mockup = Mockup.objects.filter(id=result.result)
        shirts_url = []
        if mockup.exists():
            for dress in mockup.first().dress_set.all():
                obj = dict()
                obj['image_url'] = dress.image.url
                obj['created_at'] = '2025-09-18'
                shirts_url.append(obj)
        response = {
            "task_id": task_id,
            "status": result.status,
            "result": shirts_url
        }
        return Response(response)