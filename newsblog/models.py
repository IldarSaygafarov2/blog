from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User
from blog import settings


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.EmailField(default='None', null=True, blank=True)
    photo = models.ImageField(upload_to='profile/', verbose_name='Фотография', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}, {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    ingredients = models.TextField(blank=True, verbose_name='Ингридиенты')
    steps = models.TextField(default='Здесь скоро появится рецепт', verbose_name='приготовление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    watch = models.IntegerField(default=0, verbose_name='Просмотры')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPkAAADKCAMAAABQfxahAAAAMFBMVEX29vbHx8fExMTX19f5+fnt7e3R0dHh4eHw8PD19fXn5+fLy8vT09Pd3d3l5eXg4OBxvuVsAAAE9UlEQVR4nO2d6ZajIBBGBUFFXN7/badj95yAWSzAtor0d/9OxsMNkaUoqpsGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALzG0OBu5tkYN85Td8zU9sMnyRs3K60VCa07+zHupldE7R/5yXE3+SSmJO+Nz+j2Ll1cacvd6nJMmyH+xcDd8GLGPHHVVf9793niSo/cLS8kt8ur73TT5YorXfebPmR3udJzzZ1u1nxzpao2zx3ftk6veU63JV2u2no73bQl4kpVvHwvE9cLd/vJ7KMM+ZP5N10NYQtjnF36tY/In8x/mKPHrf0yDo0sfTPMXj9SKq6ePbMd5cibYTrBkv51+EWIupkv1P5270QE65y/WvzmPvKrD9drb+o9t7orWZ8WqTO/7AW70GJ11mV92V6sEM/Z6Y5RXOmVT/36+SyGTbxpeMUZdzQLrzlfkLJ0+12M5trAF8WaTjHnisk7ZnG+0b0gpHySOVdguiC+uO20/Rdl23iuGGWuuVbTaoefAJOzS+tz7asy16q1TRxRM2bo87a6FZlrvzyNJRljc87ZqzHXfnwdP73FtD7VXM/vn2ds6m++DnPtCWk/iT/5Ksz1RHmkSdsK1GBOXXQY+2Hm9NWWSQlpyjdPWmYmqIs3148tNI2z4zjawT3Mc4b+jYo373b/0TRj+/8cTnXr/sCEPsyJN4+znLbM5+BfH7ObyXmTws13ZwJmfcx81pOLHWji0s3jaNnwfJ22+3qIOQeyzaOMvtfTdTz8E89uZJuHrXs3bMcTQPqzr4TUuqjL307VUa/TOl20+RQ27n2wNjoUJ73pks3DwPDhZBXFzykhbcnmKuXz4atOOrOTbB66HL+64aCQ+PRLIbQtPPRLVTn+tGjzeyfSTuHub7qZqjZXaX0YDoiUF12webByTV6bEOY1weZB03qSuU/6quSaB8sy6mH7/UUnJOEINr/n61EGLBUvZqo2v09qxN1XOBnAvErz/u5B/LUHq7iqzf/sCBc0jZgo6u+PJySjCDaf/uxKJliYkDKpwiGR8CMRbK7TdiDR0F73jiUMyVDiS8HbYQhflGDzKDJxHF8Ks/Urj0yEYzWh04OtXfXRqLAXD5dx4TKGlFQr2Txq3MHwHqWxJj/8SmgnDcHm6/3JuA5D87Qln2zz6OTkzcm4jk7ZadnEos3j44PX6nHuFHGVL9s8bp6xz+uG7TJpch59IdTMgfhKnXtyxrTPEqTelhBuHs3pNy27u7Stfb/7BPU2mHTzh9So6KK+f7hKT0+Okm7+5L7JltG/znP/rHwCPSFOvPmLi8MvamYkXG+Wb55yUz7lXncF5vTr4kkX2mswJ6a+pqU612H+tTp1h+00tMO3ysy/OHjZzZBaJrQa87fle41Lv81ejfltX/LC3bgn6bCfZH7r9+Uhpf12Wy3DuzLzLat7tu5e/8suedr1mW/yWvmpbdup8yVXcrnM/+4tbKbCSYE51817yinI75pzVVsgJgP8ojlbGeDEtebp8NVPYi2exFo+ibmgDFs5mYZ5XmMtec1bMovP+wZfGSHuov5sqxn28u4JF4fPFecv9J10U/48ce4e33AZf2On0PsornUVZry02K1Ws6DC7uOkzqhgfWyttV+PY7hXYhrbz+2vs46DxCruxL+aVwS3IwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4Br+AYSFRdOsVUwBAAAAAElFTkSuQmCC'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'