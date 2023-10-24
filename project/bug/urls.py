from django.urls import path
from . import views

app_name = "bug"
urlpatterns = [
    path('register/', views.BugCreateView.as_view(), name='register_bug'),
    path('<int:pk>/', views.BugDetailView.as_view(), name='view_bug'),
    path('list/', views.BugListView.as_view(), name='list_bug'),
]
