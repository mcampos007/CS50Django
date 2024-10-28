from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("mario", views.mario, name="mario"),
    # path("karina", views.karina, name="karina")
    path("<str:name>", views.greet, name="greet")
]