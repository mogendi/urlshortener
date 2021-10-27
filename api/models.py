from django.db import models, transaction
import hashlib

# Create your models here.
class Url(models.Model):
    url_id     = models.CharField(max_length=255, blank=True, null=False, unique=True)
    url_actual = models.CharField(max_length=4096, blank=False, null=False)
    url_clicks = models.IntegerField(null=False, blank=True, default=1)

    def save(self, *args, **kwargs):
        if not self.pk and self.url_id == "" or len(self.url_id) < 1:
            self.url_id = hashlib.md5(self.url_actual.encode('utf-8')).hexdigest()[:8]
        super(Url, self).save(*args, **kwargs)

    def __str__(self):
        return self.url_id
    
    # Click incrementer
    def inc(self):
        with transaction.atomic():
            self.url_clicks += 1
            self.save()