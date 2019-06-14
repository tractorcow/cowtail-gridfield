from django.conf.urls import include, url
from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.core import hooks
from wagtail.core.models import Page

from . import urls


@hooks.register('register_admin_urls')
def register_page_gridfield():
    return [
        url(r'^pages/(?P<recordid>\d+)/edit/', include(urls), kwargs={'model': Page}),
    ]


@hooks.register('insert_editor_css')
def register_gridfield_css():
    return format_html(
        '<link rel="stylesheet" href="{}" />',
        static('cowtail/dist/cowtail.css')
    )
