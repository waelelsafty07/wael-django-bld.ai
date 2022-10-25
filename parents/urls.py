from django.urls import path
from .views import Parent, ParentID

urlpatterns = [
    path('', Parent.as_view()),
    path('<int:id>', ParentID.as_view())
]
