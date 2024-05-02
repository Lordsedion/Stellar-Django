from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('home', CreateTextView.as_view()),
    path('file', CreateFileView.as_view()),
    path("signup", CreateUserView.as_view(), name="create_user"),
    path('login/', UserLoginView.as_view(), name='login'),
]
