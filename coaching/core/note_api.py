from rest_framework import serializers, viewsets
from .models import Dummy

class NoteSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Dummy
        fields = ('id', 'title', 'description', 'created_at', 'created_by')


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Dummy.objects.all()
    serializer_class = NoteSerialiser