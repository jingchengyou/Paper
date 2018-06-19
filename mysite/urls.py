from django.urls import path

from . import views


app_name = 'story'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.login, name='login'),
    path('register/', views.to_register, name='to_register'),
    path('register_main/', views.getAuthorInfo, name='getAuthorInfo'),
    path('book/<str:title>/', views.booksummary, name='book_summary'),
    path('catalog', views.catalog, name='catalog'),
    path('content', views.content, name='content'),
    path('person/<int:num>/', views.person_info, name='person_info'),
    path('push', views.push_success, name="push_success"),
    path('group/<str:title>', views.add_group, name="add_group")
]
