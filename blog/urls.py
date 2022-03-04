from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about,  name='about'),
    path('view-all-posts/', ViewAllPosts.as_view(),  name='view-all'),
    path('blog/<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
    path('category/<str:slug>/', BlogByCategory.as_view(), name=" category"),
    path('tag/<str:slug>/', BlogByTag.as_view(), name="tag"),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('search/', Search.as_view(), name='search'),
    path('register/', register, name='register'),
    path('addpost/', addpage, name='add_post'),
    path('accounts/profile/', profile, name='profile'),
]


