from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "weblearning"
urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/login/"), name="logout"),
    path("weblearning/", views.index, name="index"),
    path("weblearning/docs/<str:doc_type>/", views.docs, name="docs"),
    path("weblearning/playground", views.playground, name="playground"),
    path("weblearning/count", views.count, name="count"),
    path("weblearning/table", views.table, name="table"),
    path("weblearning/table/api/data", view=views.table_api_data, name="api_data"),
]
