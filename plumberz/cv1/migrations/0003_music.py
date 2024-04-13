# Generated by Django 5.0.3 on 2024-04-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv1', '0002_alter_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('singer_name', models.CharField(max_length=130)),
                ('image', models.ImageField(upload_to='static/images/')),
            ],
        ),
    ]