import requests
from django.shortcuts import render
from django.conf import settings

def menu_page(request)
    """
    View function for the homepage.
    This function fetches menu data from your API and passes it to the template.
    """

    all_items=Item.objects.all()

    context={
        'menu_items': all_items,
        'restaurant_name': settings.RESTAURANT_NAME,
    }


    return render(request, 'home/menu.html', context)   


