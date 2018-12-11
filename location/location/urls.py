from django.conf.urls import include, url
from django.contrib import admin
from login import views as v1
from registe import views as v2
from registe import views as v2
from mainApp import views as v3
from offline import views as v4

urlpatterns = [
    # Examples:
    # url(r'^$', 'location.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^login/',v1.isValide),
    url('^registe/',v2.addUser),
    url('^mainApp/',v3.sendLocation),
    url('^offline/',v4.setOff),
    url('^getlocation/',v3.getLocation),
    url('^download/',v3.dload),
]
