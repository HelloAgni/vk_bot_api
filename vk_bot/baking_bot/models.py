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
    """Типы выпечки"""
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
    """Описание и рецепт выпечки"""
    title = models.CharField('Название выпечки', max_length=100)
    description = models.TextField('Описание и рецепт выпечки')
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
