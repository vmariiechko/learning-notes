from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreatelView, BlogUpdatelView, BlogDeletelView


urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeletelView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdatelView.as_view(), name='post_edit'),
    path('post/new/', BlogCreatelView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]
