from cards.views import CardsView
from django.urls import path

urlpatterns = [
    path("", CardsView.as_view()),
]
