from django.db import models


class Application(models.Model):
    application_name = models.TextField()
    application_url = models.URLField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.application_name


class Developer(models.Model):
    developer = models.TextField()
    developer_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.developer


class Person(models.Model):
    person_name = models.TextField()
    person_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.person_name


class Platform(models.Model):
    platform = models.TextField(
        help_text="Platform where code is redeemed, such as Steam or GOG"
    )
    platform_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.platform


class Publisher(models.Model):
    publisher = models.TextField()
    publisher_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.publisher
