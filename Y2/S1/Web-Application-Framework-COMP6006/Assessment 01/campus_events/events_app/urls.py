from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('events/', views.event_list, name='events'),
    path('categories/', views.category_list, name='categories'),
    path('categories/<int:category_id>/', views.category_events, name='category_events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/create/', views.event_create, name='event_create'),
]