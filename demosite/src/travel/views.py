from django.shortcuts import render

def index(request):
    context = {
        'menupage': 'travel',
    }
    return render(request, 'travel_page.html', context)
