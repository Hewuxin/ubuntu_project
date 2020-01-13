from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from api.models import Book


def index(request):
    data = {
        "status": 200,
        'message': 'index'
    }
    return JsonResponse(data=data)


@csrf_exempt
def books(request):
    if request.method == "POST":
        b_name = request.POST.get("b_name")
        b_price = request.POST.get("b_price")
        book = Book()
        book.b_name = b_name
        book.b_price = b_price
        book.save()
        data = {
            'status': 201,
            'message': "update success",
            'data': book.book_to_dict()
        }
        return JsonResponse(data=data)
    if request.method == "GET":
        book_dict = []
        book_list = Book.objects.all()
        for book in book_list:
            book_dict.append(book.book_to_dict())
        data = {
            'status': 200,
            'message': 'get success',
            'data': book_dict
        }

        return JsonResponse(data=data)


@csrf_exempt
def book(request, bookid):
    if request.method == "GET":
        book_obj = Book.objects.get(pk=bookid)
        data = {
            "status": "200",
            "message": "get success",
            "res": book_obj.book_to_dict()
        }
        return JsonResponse(data=data)
    if request.method == "DELETE":
        book_obj = Book.objects.get(pk=bookid)
        book_obj.delete()

        data = {
            'status': 204,
            "message": "delete success",
            "res": {}
        }
        return JsonResponse(data=data)
