from django.shortcuts import render
import requests

from utility.constants import ENDPOINT


def home(request):
    try:
        response = requests.get(ENDPOINT)

        if response.status_code == 200:
            dict_output = response.json() 
            all_news_items = dict_output["channel"]["item"]
            return render(request, "index.html", {
                "data": all_news_items
            })

        return render(request, "index.html", {"msg": "URL not succeed!"})
    except:
        return render(request, "index.html", {"msg": "URL not working"})

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def faqs(request):
    return render(request, "faqs.html")
    