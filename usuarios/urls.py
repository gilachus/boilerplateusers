import django
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import SignupView, success, GreetingView, MyFormView


urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    path('success/', success, name="success"),
    path('about/', GreetingView.as_view(greeting="G'day")),
    path('myform/', login_required(MyFormView.as_view()), name="myform"),
]