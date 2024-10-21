from django.db import models
from pytils.translit import slugify
from datetime import datetime

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)
    created_at = models.DateTimeField("Дата и время создания", default=datetime.now)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Job(models.Model):
    title = models.CharField("Название афиши", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию") 
    company = models.CharField("Название компании", max_length=100, null=False, blank=False)
    salary = models.CharField("Оклад", max_length=80)
    description = models.TextField("Описание афиши")
    image = models.CharField("URL-фото", max_length=500)
    address = models.CharField("Адрес", max_length=100)
    phone = models.CharField("Телефон", max_length=14)
    email = models.CharField("E-mail", max_length=100)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Афиша"
        verbose_name_plural = "Афиши"

    def __str__(self):
        return self.title

class Guide(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание прошлых афиш")
    image = models.CharField("URL-фото", max_length=500)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Прошлая афиша"
        verbose_name_plural = "Прошлые афишы"

    def __str__(self):
        return self.title