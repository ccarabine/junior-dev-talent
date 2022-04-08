"""junior_dev_talent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('forum/', include('forum.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'forum.views.error_404_view'
handler500 = 'forum.views.error_500_view'
handler404 = 'home.views.error_404_view'
handler500 = 'home.views.error_500_view'
handler404 = 'products.views.error_404_view'
handler500 = 'products.views.error_500_view'
handler404 = 'profiles.views.error_404_view'
handler500 = 'profiles.views.error_500_view'
handler404 = 'checkout.views.error_404_view'
handler500 = 'checkout.views.error_500_view'

