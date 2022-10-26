from django.urls import path, include

from .views import SubjectsDetailsView, SubjectsView
urlpatterns = [
    path('', SubjectsView.as_view()),
    path('<int:pk>', SubjectsDetailsView.as_view()),
]
