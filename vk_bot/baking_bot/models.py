from django.db import models


class SimpleText(models.Model):
    """Команды для бота и описание"""
    title = models.CharField('Заголовок команды', max_length=100)
    description = models.TextField('Описание команды')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Команда для бота'
        verbose_name_plural = 'Команды для бота'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'description'],
                name='uniq_answer'
            )
        ]

    def __str__(self):
        return f'{self.title} - {self.description}'


class BakingType(models.Model):
    """Типы десерта"""
    type = models.CharField(
        'Тип десерта',
        max_length=100,
        unique=True
    )

    class Meta:
        ordering = ('type',)
        verbose_name = 'Тип десерта'
        verbose_name_plural = 'Типы десертов'

    def __str__(self):
        return self.type


class Baking(models.Model):
    """Описание десерта"""
    title = models.CharField('Название десерта', max_length=100)
    description = models.TextField('Описание и рецепт десерта')
    image = models.ImageField(
        'Изображение десерта',
        upload_to='baking_bot/images'
    )
    type = models.ForeignKey(
        BakingType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Тип десерта',
        related_name='baking'
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Десерт'
        verbose_name_plural = 'Десерты'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'description'],
                name='uniq_baking'
            )
        ]

    def __str__(self):
        return f'{self.title} - {self.description}'
