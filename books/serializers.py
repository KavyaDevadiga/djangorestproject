from rest_framework import serializers
from books.models import Bookstore
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Bookstore
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    books=serializers.HyperlinkedRelatedField(many=True,view_name='book-detail',queryset=Bookstore.objects.all())
    class Meta:
        model=User
        fields=['id','username','books']