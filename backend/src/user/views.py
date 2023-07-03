from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Account
from .serializer import AccountSerializer
from django.db import transaction


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReadUserView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, format=None):
        return Response(
            data={
                "id": request.user.id,
                "username": request.user.email,
                "email": request.user.email,
            },
            status=status.HTTP_200_OK,
        )
