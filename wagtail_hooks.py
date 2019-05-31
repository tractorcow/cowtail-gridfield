from django.conf.urls import include, url
from wagtail.core import hooks
from wagtail.core.models import Page

from . import urls


@hooks.register('register_admin_urls')
def register_page_gridfield():
    return [
        url(r'^pages/(?P<recordid>\d+)/edit/', include(urls), kwargs={'model': Page}),
    ]
