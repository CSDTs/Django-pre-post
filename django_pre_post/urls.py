from django.conf.urls import url
from django.contrib import admin
from django_pre_post.views import FillOutQuestionaire, FramelessQuestionaire

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^questionaire/(?P<pk>\d+)/$', FillOutQuestionaire.as_view(), name='fill-out-questionaire'),
    url(r'^embed-questionaire/(?P<pk>\d+)/$', FramelessQuestionaire.as_view(), name='embed-questionaire'),
]
