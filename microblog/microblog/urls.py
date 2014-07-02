from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^microblog/', include('microblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r"^$", views.HomepageView.as_view(), name="home"),
    url(r"^blog/", include("blog.urls", namespace="blog")),

    # url(r"^$", TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', include(admin.site.urls)),
)

# In real life we wouldn't want to do this.
# Serving patterns files through python is much slower than serving
# them through an actual website, like apachi.
urlpatterns += patterns('',
    (r'^static/(.*)$','django.views.static.serve', {
            'document_root': settings.STATIC_ROOT
    }),
)
