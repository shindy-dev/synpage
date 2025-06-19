from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "weblearningapp/index.html")


def playground(request):
    return render(request, "weblearningapp/pages/playground.html")


def count(request):
    return render(request, "weblearningapp/pages/count.html")


def table(request):
    return render(request, "weblearningapp/pages/table.html")
