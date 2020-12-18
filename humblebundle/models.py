from django.db import models


class Developer(models.Model):
    developer = models.TextField()
    developer_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.developer


class Publisher(models.Model):
    publisher = models.TextField()
    publisher_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.publisher


class Bundle(models.Model):
    bundle_name = models.TextField(blank=True, null=True)
    bundle_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.bundle_name


class Application(models.Model):
    application_name = models.TextField()
    application_url = models.URLField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.application_name


class Person(models.Model):
    person_name = models.TextField()
    person_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.person_name


class HumbleItem(models.Model):
    application = models.ForeignKey(Application, on_delete=models.DO_NOTHING)
    developer = models.ManyToManyField(Developer)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    bundle = models.ForeignKey(Bundle, on_delete=models.DO_NOTHING)
    date_added = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    claimed = models.BooleanField(default=False)
    claimed_by = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    date_claimed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.application.application_name
