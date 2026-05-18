from django.shortcuts import render
from globals.utils import Utils
import globals.baseapi as baseapi

listdata = ['Article 1', 'article 2', 'article 3']

def index(request):
    api = baseapi.apilogin
    data = {
        'menupage': 'article',
        'data': listdata,
        'text': getData(),
        'test': Utils.testVoid(1, 3),
        'api': api
    }
    return render(request, 'article_page.html', data)

def getData():
    return 'this data in function'
