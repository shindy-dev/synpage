from django.urls import path

from . import views

app_name = "weblearning"
urlpatterns = [
    path("weblearning", views.index, name="index"),
    path("weblearning/playground", views.playground, name="playground"),
    path("weblearning/count", views.count, name="count"),
    path("weblearning/table", views.table, name="table"),
    path("weblearning/table/api/data", view=views.table_api_data, name="api_data"),
    path("weblearning/docs/<str:doc_type>", views.docs, name="docs"),
]
