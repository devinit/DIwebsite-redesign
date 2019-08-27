from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)
from .models import Download, DataDownload


class DownloadAdmin(ModelAdmin):
    model = Download
    menu_icon = 'download'
    menu_order = 100
    menu_label = 'Downloads'
    list_display = ('file', 'title', 'language', )
    search_fields = ('file__title', 'title', )


class DataDownloadAdmin(ModelAdmin):
    model = DataDownload
    menu_icon = 'download'
    menu_order = 110
    menu_label = 'Data downloads'
    list_display = ('file', 'title', )
    search_fields = ('file__title', 'title', )


class DownloadsAdminGroup(ModelAdminGroup):
    menu_label = 'Downloads'
    menu_icon = 'download'
    menu_order = 130
    items = (
        DownloadAdmin,
        DataDownloadAdmin,
    )


modeladmin_register(DownloadsAdminGroup)
