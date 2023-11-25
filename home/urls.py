from django.urls import include, path

from home import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home')
]
