from django.conf.urls.i18n import i18n_patterns
from django.urls import path, re_path
from umap.urls import urlpatterns

from .views import DSFRHome, DSFRSearch, blog_article, BlogFeed


urlpatterns = (
    i18n_patterns(
        re_path(r"^$", DSFRHome.as_view(), name="home"),
        re_path(r"^search/$", DSFRSearch.as_view(), name="search"),
    )
    + urlpatterns
    + [
        path("blog/feed/", BlogFeed(), name="blog_feed"),
        path("blog/<slug:slug>/", blog_article, name="blog_article"),
    ]
)
