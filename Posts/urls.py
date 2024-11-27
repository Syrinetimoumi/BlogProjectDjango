
from django.urls import path
from .views import BlogView, BlogCreate, BlogUpdateView, BlogDeleteView

app_name = "Posts"

urlpatterns = [
    path('', BlogView.as_view(), name='default'),  # Route par défaut
    path('liste/', BlogView.as_view(), name='listhtml'),
    path('create/', BlogCreate.as_view(), name='createhtml'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='updatehtml'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='deletehtml'),
]
