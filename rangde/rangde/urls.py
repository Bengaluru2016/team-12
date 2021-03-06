"""rangde URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from features.views import img, test, sendsms
from home.views import home_page, seek_info, refer_info, rangde_admin, queries

urlpatterns = [
    url(r'^img/', img),
    url(r'^sendsms', sendsms),
    url(r'^test/', test),
    url(r'^home/', home_page),
    url(r'^seek_info/', seek_info),
    url(r'^refer_info/', refer_info),
    url(r'^admin/', admin.site.urls),
    url(r'^rangde_admin', rangde_admin),
    url(r'^queries', queries)
]
