import random
import time

from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render

def index(request):
    return render(request, "weblearningapp/index.html")


def playground(request):
    return render(request, "weblearningapp/pages/playground.html")


def count(request):
    return render(request, "weblearningapp/pages/count.html")


def table(request):
    return render(request, "weblearningapp/pages/table.html")


def table_api_data(request):
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

def docs(request, doc_type):
    valid_docs = ["html", "css", "js", "security"]
    if doc_type not in valid_docs:
        raise Http404("Document type not found.")
    return render(request, f"weblearningapp/pages/docs/{doc_type}.html")
