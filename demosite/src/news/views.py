from django.shortcuts import render
import globals.baseapi as baseapi

def index(request):
    data = {
        'menupage': 'news',
        'api': baseapi.apilogin
    }
    return render(request, 'news/news_page.html', data)
