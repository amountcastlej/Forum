from django.urls import path
from . import views
urlpatterns = [
    path('', views.root), 
    path('create_forum', views.create_new_forum), 
    path('forum/<int:forum_id>', views.get_one_forum),
    path('create_forum_post', views.create_new_forum_post)
]