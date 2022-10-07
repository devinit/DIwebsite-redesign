from wagtail.admin.panels import InlinePanel, MultiFieldPanel, FieldPanel


def metadata_panel(sources_relation='dataset_sources', topics_relation='dataset_topics'):
    return MultiFieldPanel([
            FieldPanel('meta_data'),
            InlinePanel(topics_relation, label='Topics'),
            InlinePanel('page_countries', label="Countries"),
            InlinePanel(sources_relation, label='Sources')
        ], heading='Metadata')
