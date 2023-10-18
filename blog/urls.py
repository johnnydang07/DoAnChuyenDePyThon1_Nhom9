from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.index, name='blog-index'),
    path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('post_detail2/<int:pk>/', views.post_detail2, name='blog-post-detail2'),
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='blog-post-delete'),
    path("draft/", views.ViewDraft, name="draft"),
    path('push_blog/<str:blog_id>/', views.push_draft, name='push_blog'),
]
