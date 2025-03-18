from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ItemSerializer

# Create your views here.


class ItemView(APIView):
    def get(self, request):
        return Response({"method": "get"})

    def post(self, request):
        print(request.data)
        serializer = ItemSerializer(data=request.data)
        print(serializer)
        print(serializer.is_valid(raise_exception=True))
        print(serializer.errors)
        return Response({"method": "post"})

    def delete(self, request):
        return Response({"method": "get"})

    def patch(self, request):
        return Response({"method": "get"})
