from django.urls import path

from . import views

app_name = "weblearningapp"
urlpatterns = [
    path("synpage/weblearningapp", views.index, name="index"),
    path("synpage/weblearningapp/playground", views.playground, name="playground"),
    path("synpage/weblearningapp/count", views.count, name="count"),
    path("synpage/weblearningapp/table", views.table, name="table"),
    path("synpage/weblearningapp/table/api/data", view=views.table_api_data, name="api_data"),
    path("synpage/weblearningapp/docs/<str:doc_type>", views.docs, name="docs"),
]
