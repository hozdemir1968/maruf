from django.urls import path
from announce import views

app_name='announce'

urlpatterns = [
    path('index/',views.announce_index,name='index'),
    path('create/',views.announce_create,name='create'),
    path('detail/<int:id>/',views.announce_detail,name='detail'),
    path('update/<int:id>/',views.announce_update,name='update'),
    path('delete/<int:id>/',views.announce_delete,name='delete'),
]