import random
import time

from django.http import JsonResponse
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


def api_data(request):
    time.sleep(2)
    response = {
        "items": [
            {
                "ID": i,
                "Name": f"Item {random.randint(1, 1000)}",
                "Value": random.randint(1, 1000),
            }
            for i in range(1, 101)
        ]
    }

    return JsonResponse(response)
