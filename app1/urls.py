from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('author/add/', views.AuthorCreateView.as_view(), name='author-add'),
    path('author/<int:pk>/', views.AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
    path('author/<int:pk>/detail/', views.author_detail, name='author-detail'),
    path('<slug:slug>/success/', views.success, name='success'),
    path('thanks/', views.thanks, name='thanks'),
] 