from django.conf.urls import patterns, include, url
from lists import views as list_views
from lists import urls as lists_urls

urlpatterns = patterns('',
    # Examples:    
    url(r'^new$', 'views.new_list', name='new_list'),
    url(r'^(\d+)/$', 'views.view_list', name='view_list'),
    url(r'^(\d+)/add_item$', 'views.add_item', name='add_item')

    #url(r'^admin/', include(admin.site.urls)),
)
