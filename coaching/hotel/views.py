from django.shortcuts import render, get_object_or_404
from .models import AllocateTask
from .hotel_api import AllocateTaskSerializer
from rest_framework import generics

# Create your views here.
class GetTask(generics.ListAPIView):
    serializer_class = AllocateTaskSerializer

    def get_queryset(self):
        id = self.kwargs['worker_id']
        return AllocateTask.objects.filter(workerId = id)

# def GetTask(request, worker_id=None):
#     task = get_object_or_404(AllocateTask, workerId = worker_id)
#     return task