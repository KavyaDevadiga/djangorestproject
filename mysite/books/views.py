from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from books.models import Bookstore
from rest_framework.views import APIView
from books.serializers import BookSerializer,UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from books.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

class book_list(generics.ListCreateAPIView):
    def get(self,request):
         books = Bookstore.objects.all()
         serializer = BookSerializer(books, many=True)
         return JsonResponse(serializer.data, safe=False)

    def post(self,request):
         data = JSONParser().parse(request)
         serializer = BookSerializer(data=data)
         if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data, status=201)
         return JsonResponse(serializer.errors, status=400)
    queryset = Bookstore.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class book_detail(generics.RetrieveUpdateDestroyAPIView):
   

    def get(self,request,pk):
          book=Bookstore.objects.get(pk = pk)
          serializer = BookSerializer(book)
          return JsonResponse(serializer.data)

    def put(self, request, pk):
        book = Bookstore.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, pk):
        book = Bookstore.objects.get(pk=pk)
        request.data["copies"]-=1
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    queryset = Bookstore.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    
    def get(self,request):
         users = User.objects.all()
         serializer = UserSerializer(users,context={'request': request}, many=True)
         return JsonResponse(serializer.data, safe=False)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    def get(self,request,pk,):
          user=User.objects.get(pk = pk)
          serializer = UserSerializer(user,context={'request': request})
          return JsonResponse(serializer.data)
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('book-list', request=request, format=format)
    })