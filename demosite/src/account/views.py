from django.shortcuts import render

def index(request):
    context = {
        'menupage': 'account',
    }
    return render(request, 'account_page.html', context)
