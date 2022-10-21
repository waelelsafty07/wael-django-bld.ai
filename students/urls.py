
from django.urls import path

from students import views
from .views import Student, StudentID

urlpatterns = [
    path('', Student.as_view()),
    path('<int:id>', StudentID.as_view())
]
