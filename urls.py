from django.conf.urls import url

from .views import Create, Edit

# Register page admin gridfield
app_name = 'cowtail_gridfield'
urlpatterns = [
    url(r'^grid/(?P<parts>[\w/]+)/add/$', Create.as_view(), name='create'),
    url(r'^grid/(?P<parts>[\w/]+)/(?P<pk>\d+)/edit/$', Edit.as_view(), name='edit'),
]
