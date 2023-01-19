from rest_framework.serializers import ModelSerializer
from .models import *

class AktyorSerializer(ModelSerializer):
    class Meta:
        model = Aktyor
        fields = '__all__'


class KinoSerializer(ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'