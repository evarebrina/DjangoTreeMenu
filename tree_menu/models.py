from django.db import models


class Menu(models.Model):
    """
    Menu model
    """
    title = models.CharField(max_length=30, verbose_name='Menu title')
    slug = models.SlugField(max_length=30, verbose_name='Slug', blank=True, null=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    """
    Item model for menu
    """
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, verbose_name='URL', blank=True, null=True)

    def __str__(self):
        return self.title

