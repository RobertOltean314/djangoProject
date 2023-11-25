from django.urls import path
from userextend import views

urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='signup'),
]
