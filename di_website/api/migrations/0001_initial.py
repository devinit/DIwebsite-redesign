# Generated by Django 3.2.25 on 2024-07-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CookieConsentLogEntry',
            fields=[
                ('token', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('anonymised_ip_address', models.GenericIPAddressField()),
                ('first_seen', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('url', models.URLField()),
                ('user_agent', models.TextField()),
                ('choice', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Cookie Consent Log Entry',
                'verbose_name_plural': 'Cookie Consent Log Entries',
            },
        ),
    ]