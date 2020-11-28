from django.urls import path
from app.views import ViewHomePage
urlpatterns = [
    path('', ViewHomePage.as_view(), name='home'),
]