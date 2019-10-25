from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel

def metadata_panel():
    return MultiFieldPanel([
            StreamFieldPanel('meta_data'),
            FieldPanel('topics'),
            InlinePanel('page_countries', label="Countries"),
            InlinePanel('dataset_sources', label='Sources')
        ], heading='Metadata')
