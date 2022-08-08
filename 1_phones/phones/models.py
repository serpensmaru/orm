from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
