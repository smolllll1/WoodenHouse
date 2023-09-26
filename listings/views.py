from django.shortcuts import render
from main_app.models import Products, ProductCutegory
from django.core.paginator import Paginator


# Create your views here.


def listings_view(request):
    categories = ProductCutegory.objects.filter(is_visible=True)
    products = Products.objects.filter(is_visible=True, is_cpecial=True, is_signature=True)
    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "listings.html",
        context={
            "page_obj": page_obj,
            "categories": categories,
            "products": products,
        },
    )
