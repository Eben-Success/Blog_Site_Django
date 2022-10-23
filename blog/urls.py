from django.urls import path
from . import views
from .views import PostListView, PostDetailView


urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>',PostDetailView.as_view(), name='post-detail' ),
    path('about/', views.about, name='blog-about'),
]

# <app> / <model> _ <viewtype>.html