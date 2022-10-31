from django.urls import path, include

from .views import Register, SignIn
urlpatterns = [
    path('register', Register.as_view()),
    path('login', SignIn.as_view()),
]
