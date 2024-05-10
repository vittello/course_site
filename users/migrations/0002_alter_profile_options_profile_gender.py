# Generated by Django 5.0.4 on 2024-04-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Мужской пол'), ('female', 'Женский пол')], default='male', max_length=10, verbose_name='Пол пользователя'),
        ),
    ]
