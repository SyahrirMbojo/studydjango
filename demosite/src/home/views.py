from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
    context = {
        'menupage': 'home'
    }
    return render(request, 'home_page.html', context)

def detailpage(request, id):
    context = {
        'id': id
    }
    return render(request, 'home_detail_page.html', context)

