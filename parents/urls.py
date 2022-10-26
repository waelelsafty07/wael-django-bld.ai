from django.urls import path, include

from .views import ParentsDetailsView, ParentsView
urlpatterns = [
    path('', ParentsView.as_view()),
    path('<int:id>', ParentsDetailsView.as_view()),
]
