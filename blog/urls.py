from .views import  get_about, get_home, blog_detail, login_view, logout_view, signup_view, create_blog, list_blogs, update_blog, delete_blog, settings
from django.urls import path

urlpatterns = [
    path('',get_home),
    path('about/',get_about),
    path('login/',login_view),
    path('logout/',logout_view),
    path('signup/',signup_view),
    path('create-blog/',create_blog),
    path('list-blogs/',list_blogs),
    path('blog-detail/<int:pk>/',blog_detail),
    path('update-blog/<int:pk>/',update_blog),
    path('delete-blog/<int:pk>/',delete_blog),
    path('settings/',settings),
] 