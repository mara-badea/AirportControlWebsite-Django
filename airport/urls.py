from django.urls import path, include
from . import views
from users import views as user_views
urlpatterns = [
    path('', views.schedule_view, name = 'home'),
    path('add-flights/', user_views.add_flight, name = 'add-flights'),
    path('edit-flights/<int:id>/', user_views.edit_flights, name='edit-flights'),
    path('delete-flight/<int:id>/', user_views.delete_flight, name='delete-flight'),
    path('search-flights/', user_views.search_flight, name='search-flights'),
    path('add-tickets/', user_views.add_tickets, name='add-tickets'),
    path('manage-tickets/', views.ticket_view, name = 'manage-tickets'),
    path('edit-tickets/<int:id>/', user_views.edit_tickets, name='edit-tickets'),
    path('delete-ticket/<int:id>/', user_views.delete_ticket, name='delete-ticket'),
    path('ticket-search/', user_views.ticket_search, name='ticket-search'),
    path('ticket-purchase/<int:id>/', user_views.ticket_purchase, name='ticket-purchase'),#
    path('ticket-search-results/', user_views.ticket_search_results, name='ticket-search-results'),
    ]