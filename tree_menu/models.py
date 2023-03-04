from django.db import models
from django.urls import reverse


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
    named_url = models.CharField(max_length=255, verbose_name='Named URL', blank=True, null=True)
    url = models.CharField(max_length=255, verbose_name='URL', blank=True, null=True)

    def get_url(self):
        if self.named_url:
            url = reverse(self.named_url)
        elif self.url:
            url = self.url
        else:
            url = '/'

        return url

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='url_or_named_url',
                check=(models.Q(named_url__isnull=True, url__isnull=False) |
                       models.Q(named_url__isnull=False, url__isnull=True))
            ),
        ]

