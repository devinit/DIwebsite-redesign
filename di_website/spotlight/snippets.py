from django.db import models
from django.utils.text import slugify

from modelcluster.models import ClusterableModel

from wagtail.search import index

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel


@register_snippet
class Spotlight(ClusterableModel):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Spotlight"
        verbose_name_plural = "Spotlights"

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Spotlight, self).save(**kwargs)


@register_snippet
class SpotlightTheme(index.Indexed, ClusterableModel):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, blank=True, null=True)
    spotlight = models.ForeignKey(
        Spotlight,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The spotlight this theme belongs to"
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        SnippetChooserPanel('spotlight')
    ]

    search_fields = [
        index.SearchField('name'),
        index.RelatedFields('spotlight', [index.SearchField('name')])
    ]

    def __str__(self):
        return self.name + ' : ' + self.spotlight.name if self.spotlight else self.name

    class Meta:
        verbose_name = "Spotlight Theme"
        verbose_name_plural = "Spotlight Themes"

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SpotlightTheme, self).save(**kwargs)


@register_snippet
class SpotlightSource(index.Indexed, ClusterableModel):
    name = models.TextField()

    panels = [FieldPanel('name')]

    search_fields = [index.SearchField('name')]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Spotlight Source"
        verbose_name_plural = "Spotlight Sources"


@register_snippet
class SpotlightColour(ClusterableModel):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=7)

    panels = [
        FieldPanel('name'),
        FieldPanel('code')
    ]

    def __str__(self):
        return self.name + ' - ' + self.code

    class Meta:
        verbose_name = "Spotlight Colour"
        verbose_name_plural = "Spotlight Colours"


@register_snippet
class SpotlightIndicator(index.Indexed, ClusterableModel):
    ddw_id = models.CharField(max_length=255)
    name = models.TextField()
    description = models.TextField(help_text='A description of this indicator', null=True, blank=True)
    theme = models.ForeignKey(
        SpotlightTheme,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    source = models.ForeignKey(
        SpotlightSource,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    color = models.ForeignKey(
        SpotlightColour,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    range = models.CharField(max_length=100, null=True, blank=True, help_text='The range of values shown on the legend')
    value_prefix = models.CharField(max_length=100, null=True, blank=True)
    value_suffix = models.CharField(max_length=100, null=True, blank=True)
    tooltip_template = models.TextField(blank=True, null=True, help_text='Text for the tooltip.Template strings can be used to substitute values e.g. {name}')

    panels = [
        FieldPanel('ddw_id'),
        FieldPanel('name'),
        FieldPanel('description'),
        SnippetChooserPanel('theme'),
        SnippetChooserPanel('source'),
        SnippetChooserPanel('color'),
        FieldPanel('start_year'),
        FieldPanel('end_year'),
        FieldPanel('range'),
        FieldPanel('value_prefix'),
        FieldPanel('value_suffix'),
        FieldPanel('tooltip_template')
    ]

    search_fields = [index.SearchField('ddw_id'), index.SearchField('name')]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Spotlight Indicator"
        verbose_name_plural = "Spotlight Indicators"
