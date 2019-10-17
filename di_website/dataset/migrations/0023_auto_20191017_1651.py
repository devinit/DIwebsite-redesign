# Generated by Django 2.2.3 on 2019-10-17 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_auto_20191011_1357'),
        ('publications', '0022_auto_20191017_1215'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('common', '0007_country_region'),
        ('blog', '0019_auto_20191011_1357'),
        ('events', '0021_auto_20191011_1357'),
        ('home', '0035_auto_20191017_0512'),
        ('project', '0034_auto_20191011_1357'),
        ('datasection', '0021_auto_20191017_1650'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtaillinkchecker', '0005_auto_20180922_1835'),
        ('dataset', '0022_auto_20191017_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datasetpagerelatedlink',
            name='other_page',
        ),
        migrations.RemoveField(
            model_name='datasetpagerelatedlink',
            name='page',
        ),
        migrations.RemoveField(
            model_name='datasetsource',
            name='page',
        ),
        migrations.RemoveField(
            model_name='datasetsource',
            name='source',
        ),
        migrations.RemoveField(
            model_name='datasettopic',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='datasettopic',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='moreaboutrelatedlink',
            name='other_page',
        ),
        migrations.RemoveField(
            model_name='moreaboutrelatedlink',
            name='page',
        ),
        migrations.RemoveField(
            model_name='teammemberrelatedlink',
            name='other_page',
        ),
        migrations.RemoveField(
            model_name='teammemberrelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='DatasetPage',
        ),
        migrations.DeleteModel(
            name='DatasetPageRelatedLink',
        ),
        migrations.DeleteModel(
            name='DataSetSource',
        ),
        migrations.DeleteModel(
            name='DataSetTopic',
        ),
        migrations.DeleteModel(
            name='MoreAboutRelatedLink',
        ),
        migrations.DeleteModel(
            name='TeamMemberRelatedLink',
        ),
    ]
