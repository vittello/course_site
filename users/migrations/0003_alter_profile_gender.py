# Generated by Django 5.0.4 on 2024-04-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Мужской пол'), ('female', 'Женский пол')], max_length=10, verbose_name='Пол пользователя'),
        ),
    ]