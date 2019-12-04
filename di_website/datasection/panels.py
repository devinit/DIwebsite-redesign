from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel

def metadata_panel(sources_relation='dataset_sources'):
    return MultiFieldPanel([
            StreamFieldPanel('meta_data'),
            FieldPanel('topics'),
            InlinePanel('page_countries', label="Countries"),
            InlinePanel(sources_relation, label='Sources')
        ], heading='Metadata')
