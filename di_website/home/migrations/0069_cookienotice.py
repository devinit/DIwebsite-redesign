# Generated by Django 2.2.16 on 2021-07-02 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('home', '0068_auto_20210617_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookieNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('cookie_policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
            ],
        ),
    ]