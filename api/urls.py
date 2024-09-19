from django.urls import path
from api.views import difference_view

urlpatterns = [
    path("difference", difference_view, name="difference"),
]
