from django.shortcuts import render

def index(request):
    data = {
        'menupage': 'about',
        'data': 'Ini data dari views'
    }
    return render(request, 'about_page.html', data)
