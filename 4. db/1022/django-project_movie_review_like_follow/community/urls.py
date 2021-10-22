from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    # Review
    ## CRUD
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    
    ## Like
    path('<int:review_pk>/like/', views.likes, name='likes'),
    
    # Comment
    ## CD
    path('<int:review_pk>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]