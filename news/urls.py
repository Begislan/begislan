from django.urls import path
from .views import * 
from . import views

urlpatterns = [
    path('', news_home, name='news_home'),
    path('create', create, name='create'),
    path('<int:pk>', views.NewsDatailView.as_view(), name='news-datail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
]