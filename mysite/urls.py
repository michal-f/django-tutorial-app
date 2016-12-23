from django.contrib import admin
from django.conf.urls import include, url
from django.views.i18n import javascript_catalog

from .views import *


js_info_dict_app = {
    'packages': ('polls',),
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^index/', include('polls.urls', namespace="polls")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/polls/$', javascript_catalog, js_info_dict_app),
    url(r'^jsi18n/index/$', javascript_catalog, js_info_dict_app),
]
