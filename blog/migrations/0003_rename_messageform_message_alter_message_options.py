# Generated by Django 5.0.4 on 2024-05-03 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_messageform_delete_news'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MessageForm',
            new_name='Message',
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
    ]
