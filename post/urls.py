from django.urls import path
from post import views

app_name='post'

urlpatterns = [
    path('index/',views.post_index,name='index'),
    path('create/',views.post_create,name='create'),
    path('detail/<int:id>/',views.post_detail,name='detail'),
    path('update/<int:id>/',views.post_update,name='update'),
    path('delete/<int:id>/',views.post_delete,name='delete'),
]