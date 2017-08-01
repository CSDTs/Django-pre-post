from django.conf.urls import url
from django.contrib import admin
from django_pre_post.views import FillOutQuestionaire, FramelessQuestionaire
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^questionaire/(?P<pk>\d+)/$', FillOutQuestionaire.as_view(), name='fill-out-questionaire'),
    url(r'^success/',
        TemplateView.as_view(template_name='django_pre_post/successful_post.html'),
        name='successful-submission'),
    url(r'^embed-questionaire/(?P<pk>\d+)/$', FramelessQuestionaire.as_view(), name='embed-questionaire'),
]
