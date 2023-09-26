from django.urls import path
from .views import reservation_list, update_reservation

app_name = 'manager'

urlpatterns = [
	path('', reservation_list, name='reservation'),
	path('update/<int:pk>', update_reservation, name='update_reservation'),
]