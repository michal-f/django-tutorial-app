# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.core.urlresolvers import reverse

from . import views


def javascript_settings():
    js_conf = {'ajax_view': reverse('ajax-view')}
    return js_conf


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^index/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^create/$', views.CreateQuestion.as_view(), name='create_question'),
    url(r'^edit/(?P<pk>\d+)/$', views.EditQuestion.as_view(), name='edit_question'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteQuestion.as_view(), name='delete_question'),
    url(r'^ajax/$', views.ajax_view, name='ajax-view'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]