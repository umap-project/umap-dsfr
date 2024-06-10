from pathlib import Path

import frontmatter
import mistune
from dataclasses import dataclass
from django.conf import settings
from django.contrib.syndication.views import Feed
from django.http import HttpResponse
from django.template import loader
from django.template.defaultfilters import slugify
from django.urls import reverse
from umap.views import Home, Search

from .utils import each_file_from

md = mistune.create_markdown(escape=False)
BLOG_SRC = Path(__file__).parent.resolve() / "blog"


@dataclass
class Article:
    item: dict
    markdown: str
    html: str

    def __post_init__(self):
        self.title = self.item["title"]
        self.date = self.item["date"]
        self.description = self.item["description"]
        self.image = self.item["image"]
        self.image_alt = self.item["image_alt"]
        self.tags = self.item["tags"]
        self.slug = slugify(self.title)
        self.url = reverse("blog_article", args=[self.slug])

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
            item = frontmatter.load(markdown_file)
            html = md(item.content)
            page = Article(item=item, markdown=item.content, html=html)
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
        return item.html.replace('="/static', f'="{self.link}static')

    def item_link(self, item):
        return self.link + reverse("blog_article", args=[item.slug])


class BlogContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["blog_articles"] = Article.all(BLOG_SRC)
        return context


class DSFRHome(BlogContextMixin, Home): ...


class DSFRSearch(BlogContextMixin, Search): ...


def blog_article(request, slug):
    template = loader.get_template("umap/article.html")
    blog_articles = Article.all(BLOG_SRC)
    blog_article = [article for article in blog_articles if article.slug == slug].pop()
    context = {
        "blog_articles": blog_articles,
        "blog_article": blog_article,
    }
    return HttpResponse(template.render(context, request))
