from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('signout/', LogoutView.as_view(template_name='users/sign-out.html'), name='sign-out'),
    path('sign-up/', views.register, name='sign-up'),
    path('sign-in/', LoginView.as_view(template_name='users/sign-in.html'), name='sign-in'),
    path('profile/', views.profile, name='profile'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
    # path('user-posts/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('create-post', views.create_post, name='create-post')
]
