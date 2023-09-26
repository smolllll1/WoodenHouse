from django.shortcuts import render
from main_app.models import Reservation
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def office_view(request):
	# massages = Reservation.objects.filter(is_processed=False)
	return render(request, 'office_list.html', context={'reservation': 'No reservation'})