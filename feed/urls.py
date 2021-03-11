from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from feed import views

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>/', views.get_user_profile, name='user-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('new/', views.new, name='feed-new'), 
]
