from django.shortcuts import render

def home(request):
    context = {
        "data": [
            {
                "name": "anil",
                "age": 26
            },
            {
                "name": "Sunil",
                "age": 46
            },
            {
                "name": "Sanju",
                "age": 15
            },
        ]
    }

    return render(request, "index.html", context)

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def faqs(request):
    return render(request, "faqs.html")
    