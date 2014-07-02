from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r"^$", views.PostListView.as_view(), name = "list"), # Home page
    url(r"^(?P<slug>[\w-]+)/$", views.PostDetailView.as_view(), name = "detail"),
)
