from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ("id", "email", "password")

    def create(self, request):
        return Account.objects.create_user(request.get('email'), request.get('password'))
