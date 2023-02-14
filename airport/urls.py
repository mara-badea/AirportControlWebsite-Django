from django.urls import path, include
from . import views
from users import views as user_views
urlpatterns = [
    path('', views.schedule_view, name = 'home'),
    path('add-flights/', user_views.add_flight, name = 'add-flights'),
    path('edit-flights/<int:id>/', user_views.edit_flights, name='edit-flights'),
    path('delete-flight/<int:id>/', user_views.delete_flight, name='delete-flight'),
    path('search-flights', user_views.search_flight, name='search-flights'),
    ]