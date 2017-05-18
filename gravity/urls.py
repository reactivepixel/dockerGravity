"""gravity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from api import api

from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # New Track
    url(r'^tracks/new$', api.TrackHandler.as_view()),

    # View Track
    url(r'^tracks/(?P<track_id>[a-zA-Z0-9\-]+)$', api.TrackHandler.as_view()),

    # View Set
    url(r'^sets/(?P<set_id>[a-zA-Z0-9\-]+)$', api.SetHandler.as_view()),

    # View Setlist
    url(r'^setlists/(?P<setlist_id>[a-zA-Z0-9\-]+)$', api.SetlistHandler.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.UPLOADS_URL, document_root=settings.UPLOADS_ROOT)
