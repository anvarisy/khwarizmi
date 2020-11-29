from django.urls import path
from app.views import ViewCourseEvent, ViewEvent, ViewHomePage, ViewImageVideo, ViewPortfolio, ViewProduct, ViewSoftDev
urlpatterns = [
    path('', ViewHomePage.as_view(), name='home'),
    path('software-developer/', ViewSoftDev.as_view(), name='softdev'),
    path('course/<int:status>/', ViewCourseEvent.as_view(), name='course'),
    path('image-video/', ViewImageVideo.as_view(), name='image-video'),
    path('events/', ViewEvent.as_view(), name='events'),
    path('products/', ViewProduct.as_view(), name='products'),
     path('portfolio/<int:status>/', ViewPortfolio.as_view(), name='portfolio'),
]