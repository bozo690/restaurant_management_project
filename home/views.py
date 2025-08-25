import requests
from django.shortcuts import render

def home(request)
    """
    View function for the homepage.
    This function fetches menu data from your API and passes it to the template.
    """

    api_url="http://127.0.0.1/api/menu/"

    menu_data=[]
    error_message=None
    
    try:
        response=requests.get(api_url)

        response.raise_for_status()

        menu_data=response.json()

    except requests.exceptions.RequestException as e:
        error_message=f"Could not connect to make API. Please try again later. Error:{e}"
    except ValueError:
        error_message="Could not parse the response from the menu API."
    
    context={
        'menu_items':menu_data,
        'error_message':error_message,
    }

    return render(request, 'home/index.html', context)


