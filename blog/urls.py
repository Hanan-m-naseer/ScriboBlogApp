from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('all-posts/', views.all_posts, name='all_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('create-post/', views.create_post, name='create_post'),
    path('edit-post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete-post/<int:pk>/', views.delete_post, name='delete_post'),
    path('like-post-ajax/<int:post_id>/', views.like_post_ajax, name='like_post_ajax'),

    path('add-comment/<int:post_id>/', views.add_comment, name='add_comment'),

    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # DRF API Endpoints
    path('api/posts/', views.PostListCreateAPIView.as_view(), name='api_posts'),
    path('api/posts/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='api_post_detail'),
    path('api/posts/<int:pk>/like/', views.LikeToggleAPIView.as_view(), name='api_post_like'),

    path('api/posts/<int:post_id>/comments/', views.CommentListCreateAPIView.as_view(), name='api_post_comments'),
    path('api/comments/<int:pk>/', views.CommentUpdateDestroyAPIView.as_view(), name='api_comment_detail'),
]
