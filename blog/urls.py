from django.urls import pathfrom .view import BlogListView



urlpatterns = [
    path('', BlogListView.as_view(). name='none'),
]