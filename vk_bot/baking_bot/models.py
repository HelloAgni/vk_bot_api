from django.db import models


class SimpleText(models.Model):
    """Варианты ответа бота на запросы"""
    title = models.CharField('Заголовок команды', max_length=100)
    text = models.TextField('Текс команды')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Команда для бота'
        verbose_name_plural = 'Команды для бота'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'text'],
                name='uniq_answer'
            )
        ]

    def __str__(self):
        return f'{self.title} - {self.text}'


class BakingType(models.Model):
    type = models.CharField(
        'Тип выпечки',
        max_length=100,
        unique=True
    )

    class Meta:
        ordering = ('type',)
        verbose_name = 'Тип выпечки'
        verbose_name_plural = 'Типы выпечки'

    def __str__(self):
        return self.type


class Baking(models.Model):
    title = models.CharField('Название выпечки', max_length=100)
    description = models.TextField('Описание выпечки')
    image = models.ImageField(
        'Изображение выпечки',
        upload_to='baking_bot/images'
    )
    type = models.ForeignKey(
        BakingType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Тип выпечки',
        related_name='baking'
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Выпечка'
        verbose_name_plural = 'Выпечки'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'description'],
                name='uniq_baking'
            )
        ]

    def __str__(self):
        return f'{self.title} - {self.description}'