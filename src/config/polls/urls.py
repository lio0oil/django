from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("index/", views.index, name="index"),
    path("login/", TemplateView.as_view(template_name="polls/login.html")),
    path("logout/", views.logout, name="logout"),
]
