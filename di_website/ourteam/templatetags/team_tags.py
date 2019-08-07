from django import template

from di_website.blog.models import BlogArticlePage

register = template.Library()


@register.simple_tag
def user_content(author_page):
    """
    Blogs, Publications that were authored by the user
    """
    # TODO: return user publications as well
    return BlogArticlePage.objects.filter(internal_author_page=author_page).live()
