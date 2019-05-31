from django.conf.urls import url

from . import views

# Register page admin gridfield
item = views.ItemHandler()
urlpatterns = [
    url(r'^grid/(?P<parts>[\w/]+)/create/$', item.create, name='cowtail_create'),
    url(r'^grid/(?P<parts>[\w/]+)/(?P<itemid>\d+)/edit/$', item.edit, name='cowtail_edit'),
]
