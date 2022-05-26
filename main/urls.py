from django.urls import path
from . import views
from .views import *
app_name = 'main'

urlpatterns = [
    path("", Homepage.as_view()),
    path("my_profile/<username>", Profile.as_view()),
    path("profiles/<username>", Jobs.as_view()),
    path("profiles/<company_id>/<username>", Jobs.as_view()),
    path("register", Registeration.as_view()),
    path("login", Login.as_view()),
    path("logout", Logout.as_view()),
    path("job_details/<username>", Experience.as_view()),
]
