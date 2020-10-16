from wagtail.admin.edit_handlers import InlinePanel, MultiFieldPanel, StreamFieldPanel


def metadata_panel(sources_relation='dataset_sources', topics_relation='dataset_topics'):
    return MultiFieldPanel([
            StreamFieldPanel('meta_data'),
            InlinePanel(topics_relation, label='Topics'),
            InlinePanel('page_countries', label="Countries"),
            InlinePanel(sources_relation, label='Sources')
        ], heading='Metadata')
