from pathlib import Path

import frontmatter
import mistune
from dataclasses import dataclass
from django.conf import settings
from django.contrib.syndication.views import Feed
from django.http import HttpResponse
from django.template import loader
from django.template.defaultfilters import slugify
from django.views.generic.base import TemplateView
from django.urls import reverse

from umap.views import Home, Search

from .utils import each_file_from

md = mistune.create_markdown(escape=False)
BLOG_SRC = Path(__file__).parent.resolve() / "blog"
INFOLETTRES_SRC = Path(__file__).parent.resolve() / "infolettres"


@dataclass
class Article:
    item: dict
    markdown: str
    html: str
    kind: str

    def __post_init__(self):
        self.title = self.item["title"]
        self.date = self.item["date"]
        self.description = self.item.get("description")
        self.image = self.item.get("image")
        self.image_alt = self.item.get("image_alt")
        self.link = self.item.get("link")
        self.tags = self.item.get("tags", [])
        self.slug = slugify(self.title)
        if self.kind == "blog":
            self.url = reverse(self.kind, args=[self.slug])

    def __eq__(self, other):
        return self.slug == other.slug

    def __lt__(self, other: "Article"):
        if not isinstance(other, Article):
            return NotImplemented
        return self.date < other.date

    @staticmethod
    def all(source: Path):
        items = []
        for markdown_file in each_file_from(source, pattern="*.md"):
            kind = markdown_file.parts[-2]
            item = frontmatter.load(markdown_file)
            html = md(item.content)
            page = Article(item=item, markdown=item.content, html=html, kind=kind)
            items.append(page)
        return sorted(items, reverse=True)


class BlogFeed(Feed):
    title = "Actualités uMap (ANCT)"
    link = settings.SITE_URL
    description = "Derniers articles publiés sur le blog de uMap pour l’ANCT."

    def items(self):
        return Article.all(BLOG_SRC)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # Deal with relative image/links.
        return item.html.replace('="/static', f'="{self.link}/static')

    def item_link(self, item):
        return self.link + reverse("blog_article", args=[item.slug])


class MenuContextMixin:
    # Should probably move to a dedicated context processor at some point.
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["blog"] = Article.all(BLOG_SRC)
        return context


class DSFRHome(MenuContextMixin, Home): ...


class DSFRSearch(MenuContextMixin, Search): ...


def blog(request, slug):
    template = loader.get_template("umap/article.html")
    blog = Article.all(BLOG_SRC)
    article = [item for item in blog if item.slug == slug].pop()
    context = {
        "blog": blog,
        "article": article,
    }
    return HttpResponse(template.render(context, request))


def infolettres(request):
    template = loader.get_template("umap/infolettres.html")
    infolettres = Article.all(INFOLETTRES_SRC)
    blog = Article.all(BLOG_SRC)
    context = {
        "infolettres": infolettres,
        "blog": blog,
    }
    return HttpResponse(template.render(context, request))


class MentionsLegales(MenuContextMixin, TemplateView):
    template_name = "umap/mentions_legales.html"
