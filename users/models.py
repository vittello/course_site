from django.db import models
from django.contrib.auth.models import User

CHOICES = (('male', 'Мужской пол'),('female', 'Женский пол'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='icon.png', upload_to='pictures/user_img')
    gender = models.CharField('Пол пользователя', choices=CHOICES, max_length=10)
    boolean = models.BooleanField('Соглашение про отправку уведомлений на почту', default=False)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = "Профили"
        

        