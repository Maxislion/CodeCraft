# Generated by Django 5.0.3 on 2024-04-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv1', '0003_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='music_file',
            field=models.FileField(blank=True, null=True, upload_to='static/music/'),
        ),
    ]