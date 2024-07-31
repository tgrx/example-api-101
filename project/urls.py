from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("", include("mainpage.urls")),
    path("admin/", admin.site.urls),
    path("api/cards/", include("cards.urls")),
]
