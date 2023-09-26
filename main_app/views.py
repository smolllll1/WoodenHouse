from django.shortcuts import render, redirect
from .models import ProductCutegory, Products, Agents, New
from .forms import ReservationForm


# Create your views here.
def main_view(request):

    if request.method == 'POST':
        form_reserve = ReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/#')

    categories = ProductCutegory.objects.filter(is_visible=True)
    products = Products.objects.filter(is_visible=True, is_cpecial=True, is_signature=True)
    agents = Agents.objects.filter(is_visible=True)
    news = New.objects.filter(is_visible=True)
    form_reserve = ReservationForm()
    return render(request, 'main_page.html', context={
            'categories': categories,
            'products': products,
            'agents': agents,
            'form_reserve': form_reserve,
            'news': news,
        },
    )
