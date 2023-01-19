from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
# Create your views here.

class KinoModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer
    @action(methods=['GET'], detail=True)
    def comments(self,request,pk):
        comments = Comment.objects.filter(kino__id=pk)
        serializer = CommentSerializer(comments, many=True)
        data = {
            "Success":serializer.data
        }
        return Response(data)


class AktyorModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Aktyor.objects.all()
    serializer_class = AktyorSerializer


class CommentModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request):
        comment = request.data
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid():
            serializer.save(user=request.user)
            data = {"Success": serializer.data}
            return Response(data)
        return Response({"Errors": serializer.errors})