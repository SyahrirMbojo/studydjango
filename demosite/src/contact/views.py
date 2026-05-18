from django.shortcuts import render

def index(request):
    context = {
        'menupage': 'contact',
    }
    return render(request, 'contact_page.html', context)
