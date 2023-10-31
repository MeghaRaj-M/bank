from django.db import models


class District(models.Model):
    district = models.CharField(max_length=300)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.district


class Branch(models.Model):
    branch = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch
