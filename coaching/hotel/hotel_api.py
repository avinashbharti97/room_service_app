from rest_framework import serializers, viewsets
from rest_framework import generics
from .models import Asset, Worker, Task, AllocateTask

class AssetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Asset
        fields = ('id', 'title', 'description')


class WorkerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Worker
        fields = ('id', 'name', 'description')


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description')

class AllocateTaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AllocateTask
        fields = ('id', 'assetId', 'taskId','workerId')


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AllocateTaskViewSet(viewsets.ModelViewSet):
    queryset = AllocateTask.objects.all()
    serializer_class = AllocateTaskSerializer

class GetTaskViewSet(viewsets.ModelViewSet):
    # queryset = AllocateTask.objects.filter(workerId)
    serializer_class = AllocateTaskSerializer

    def get_queryset(self):
  
       
        return AllocateTask.objects.filter(workerId)