from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("middleware/<slug:slug>/", views.middleware_detail, name="middleware_detail"),
]
