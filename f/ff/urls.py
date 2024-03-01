from ff import views
from django.urls import path

urlpatterns = [
    path('', views.home, ),
    path('search_id/', views.search_id ),
    path('search_name/', views.search_name ),
    path('edit/<int:id>/',  views.edit),
    path('delete/<int:id>/',  views.delete),

]