from django.db import models

class Course(models.Model):
    slug = models.SlugField('Уникальное название курса', unique=True)
    title = models.CharField('Название курса', max_length=120)
    desc = models.TextField('Описание курса')
    image = models.ImageField('Изображение курса', default='default.png', upload_to='course_image')
    
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
    
    
