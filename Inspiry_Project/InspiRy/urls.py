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
    path('contact/', views.contact_view, name='contact'),
    path('delete/<str:pk>/', views.deletePost, name='deletePost'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('etc/', views.etc_view, name='etc'),
    path('search/', views.search_posts, name='search_posts'),
]
    
    
    


# urlpatterns = [
#     path('create/', create_post, name='create_post'),
#     path('create/', views.createPost, name='createPost'),
# ]
