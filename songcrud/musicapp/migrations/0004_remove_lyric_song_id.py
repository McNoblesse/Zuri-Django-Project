# Generated by Django 4.1.2 on 2022-10-28 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_song_date_released'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lyric',
            name='song_id',
        ),
    ]