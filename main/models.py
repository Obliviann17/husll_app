from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    main_price = models.CharField(max_length=10)
    discount_price = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=250)
    photo = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    available = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_page', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = 'Товари'
        verbose_name_plural = 'Товари'
        ordering = ['name', ]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категорії'
        verbose_name_plural = 'Категорії'