from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_bug, name='register_bug'),
    path('<int:bug_id>/', views.view_bug, name='view_bug'),
    path('list/', views.list_bug, name='list_bug'),
]
