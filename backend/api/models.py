from django.db import models


class Product(models.Model):
    """Модель для создания товара."""
    
    title = models.CharField('Название', max_length=120)
    description = models.TextField('Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def _str_(self):
        return self.title
