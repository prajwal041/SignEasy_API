from rest_framework import serializers

from .models import Books, User

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'