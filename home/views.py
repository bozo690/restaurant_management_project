import requests
from django.shortcuts import render
from django.conf import settings

def mhome(request):
    """
    View function for the homepage.
    This function fetches menu data from your API and passes it to the template.
    """
    api_url='http://127.0.0.1:8000/api/menu/'

    menu_data=[]
    error_message=None
    
    try:
        response=requests.get(api_url)
        response.raise_for_status()
        menu_data=response.json()
    except requests.exceptions.RequestException as e:
        error_message=f"Could not connect to the menu API. Please try again  later. Error:{e}"
    except ValueError:
        error_message= "Could not parse the response from the menu API."

    context={
        'menu_items': menu_data,
        'error_message': error_message,
        'restaurant_name': settings.RESTAURANT_NAME,
        'restaurant_address': settings.RESTAURANT_ADDRESS,
        'google_maps_url': settings.GOOGLE_MAPS_EMBED_URL,
    }


    return render(request, 'home/index.html', context)   


