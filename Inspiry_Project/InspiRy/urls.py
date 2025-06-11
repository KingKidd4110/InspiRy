from django.urls import path
from . import views


urlpatterns = [
    path('', views.testPage, name='testPage'),
    path('home', views.homePage, name='homepage'),
    path('posts/<str:pk>/', views.postPage, name='posts'),
    path('navbar', views.navigationPage, name='navbar'),
    path('footer', views.footerPage, name='footer'),
    path('userprofile', views.userprofilePage, name='userprofile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('post_form/', views.createPost, name='createPost'),
    path('delete/<str:pk>/', views.deletePost, name='deletePost'),
]
    
