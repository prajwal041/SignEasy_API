import requests,json,re
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse,Http404
from rest_framework import viewsets,generics,status
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Books, User
from django.db.models import F
from .serializers import BooksSerializers,UserSerializers

# @api_view(['GET', 'POST'])
# def borrow(request):
#     """
#     Borrow operations
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         books = Books.objects.update(no_copies=F('no_copies')-1)
#         serializer = BooksSerializers(books, many=True)
#         return Response(serializer.data)

@api_view(['GET', 'POST'])
def returns(request):
    """
    Return operations
    :param request:
    :return: serialized Book data
    """
    if request.method == 'GET':
        books = Books.objects.filter(id__in=statements).update(no_copies=F('no_copies')+1)
        serializer = BooksSerializers(books, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def books_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializers(books, many=True)
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BooksSerializers(data=request.data)
        records = []
        if serializer.is_valid():
            serializer.save()
            d = {"status_code": 201, "status": "success"}

            d1 = {}
            d1["books"] = serializer.data
            records.append(d1)
            d["data"] = records
            return Response(d, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def members_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        members = User.objects.all()
        serializer = UserSerializers(members, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        records = []
        if serializer.is_valid():
            serializer.save()
            d = {"status_code": 201, "status": "success"}

            d1 = {}
            d1["members"] = serializer.data
            records.append(d1)
            d["data"] = records
            return Response(d, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReturnDetail(APIView):

    """
    Retrieve return book event instance.
    """

    def get_object(self, pk):
        try:
            Books.objects.filter(book_id=pk).update(no_copies=F('no_copies')+1)
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = BooksSerializers(event)
        d = {"status": "Returned successfully"}
        records = []
        records.append(serializer.data)
        d["data"] = records
        pickup_records = json.dumps(d, indent=4)
        return HttpResponse(pickup_records, content_type="application/json")


class BorrowDetail(APIView):

    """
    Retrieve, update or delete a event instance.
    """

    def get_object(self, pk):
        try:
            Books.objects.filter(book_id=pk).update(no_copies=F('no_copies')-1)
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = BooksSerializers(event)
        d = {"Remainder": "3 days", "status": "Issued Successfully"}
        records = []
        records.append(serializer.data)
        d["data"] = records
        pickup_records = json.dumps(d, indent=4)
        return HttpResponse(pickup_records, content_type="application/json")

class BookDetail(APIView):

    """
    Retrieve, update or delete a event instance.
    """

    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = BooksSerializers(event)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializers(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = BooksSerializers(event, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MemberDetail(APIView):

    """
    Retrieve, update or delete a event instance.
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = UserSerializers(event)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializers(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = UserSerializers(event, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


