from django.db import models

from core.models import Person, Application, Publisher, Developer


class HumbleBundle(models.Model):
    bundle_name = models.TextField(blank=True, null=True)
    bundle_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.bundle_name


class HumbleItem(models.Model):
    application = models.ForeignKey(Application, on_delete=models.DO_NOTHING)
    developer = models.ManyToManyField(Developer)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    bundle = models.ForeignKey(HumbleBundle, on_delete=models.DO_NOTHING)
    redemption_platform = models.TextField(
        help_text="Platform where code is redeemed, such as Steam or GOG"
    )
    date_added = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    is_gift = models.BooleanField(default=False)
    is_claimed = models.BooleanField(default=False)
    claimed_by = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    date_claimed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.application.application_name
