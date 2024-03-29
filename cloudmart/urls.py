"""cloudmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    #sets language preference see https://docs.djangoproject.com/en/1.10/topics/i18n/translation/
    url(r'^i18n/', include('django.conf.urls.i18n')),

    #Braintree integration
    #url(r'^payment-details/', include('cloudmart.checkout.urls')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', include(admin.site.urls)),

    #from application(oscar.app) import the url paths
    url(r'', include(application.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)