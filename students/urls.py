from django.urls import path, include

from .views import StudentsDetailsView, StudentsView
urlpatterns = [
    path('', StudentsView.as_view()),
    path('<int:pk>', StudentsDetailsView.as_view()),
]
