
from django.urls import path
from students import views
from .views import Subject, SubjectID

urlpatterns = [
    path('', Subject.as_view()),
    path('<int:id>', SubjectID.as_view())
]
