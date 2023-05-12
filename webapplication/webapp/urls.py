from django.urls import path
from . import views
app_name = 'webapp'
urlpatterns = [
    path('', views.Movie, name='movie'),
    path('movie/<int:ID>/', views.details, name='details'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:ID>/', views.update, name='update'),
    path('delet/<int:ID>/', views.delet, name='delet')
]