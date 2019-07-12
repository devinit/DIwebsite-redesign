from django import template
from di_website.blog.models import BlogArticlePage

register = template.Library()


@register.simple_tag
def get_blog_articles():
    return BlogArticlePage.objects.all().live()
