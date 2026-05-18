from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.home.urls')),
    path('about/', include('src.about.urls')),
    path('article/', include('src.article.urls')),
    path('news/', include('src.news.urls')),
    path('travel/', include('src.travel.urls')),
    path('contact/', include('src.contact.urls')),
    path('account/', include('src.account.urls')),
]
