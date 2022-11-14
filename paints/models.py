from django.db import models
from django.urls import reverse


class Collection(models.Model):
    title = models.CharField("Коллекция", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Коллекции"
        verbose_name_plural = "Коллекция"


class Material(models.Model):
    title = models.CharField("Материал", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материал"


class Year(models.Model):
    title = models.CharField("Год", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Год"
        verbose_name_plural = "Год написания"


class Orientation(models.Model):
    title = models.CharField('Ориентация', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ориентация"
        verbose_name_plural = "Ориентация"


class Paint(models.Model):
    title = models.CharField("Название", max_length=100)
    photo = models.ImageField(
        upload_to='media/img/photo/%Y/%m/%d/', verbose_name="Фото", blank=True)
    description = models.TextField("Описание", blank=True)
    price = models.FloatField("Цена", blank=True)
    pub_date = models.DateTimeField("Дата публикации", auto_now=True)
    in_stock = models.BooleanField(default=True, verbose_name="В наличии ")
    year = models.ForeignKey(
        Year, on_delete=models.PROTECT, null=True, verbose_name="Год")
    materials = models.ForeignKey(
        Material, on_delete=models.PROTECT, null=True, verbose_name="Материал")
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, null=True, verbose_name="Коллекция")
    author_repeat = models.BooleanField("Авторский повтор", default=False)
    orientation = models.ForeignKey(
        Orientation, on_delete=models.PROTECT, null=True, verbose_name="Ориентация")

    def get_absolute_url(self):
        return reverse('paint', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Картину"
        verbose_name_plural = "Картины"
