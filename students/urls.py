
from django.urls import path

from students import views
from .views import Student

urlpatterns = [
    path('', Student.as_view()),
    path('<int:id>', Student.as_view())
]
