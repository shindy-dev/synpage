from django.urls import path

from . import views

app_name = "weblearningapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("pages/playground", views.playground, name="playground"),
    path("pages/count", views.count, name="count"),
    path("pages/table", views.table, name="table"),
    path("api/data", view=views.api_data, name="api_data"),
]
