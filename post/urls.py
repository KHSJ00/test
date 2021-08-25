from django.urls import path
from post.views import post_list, post_detail, post_edit, post_delete, post_new, post_list_staff, post_not_allowed, post_detail_staff

app_name = 'post'

urlpatterns = [
    path('post_list', post_list, name='post_list'),
    path('post_list_staff', post_list_staff, name='post_list_staff'),
    path('post/<pk>/', post_detail, name='post_detail'),
    path('new/', post_new, name='post_new'),
    path('post/<pk>/edit/', post_edit, name='post_edit'),
    path('post/<pk>/delete/', post_delete, name='post_delete'),
    path('post_not_allowed', post_not_allowed, name='post_not_allowed'),
    path('post/<pk>/staff', post_detail_staff, name='post_detail_staff'),
]