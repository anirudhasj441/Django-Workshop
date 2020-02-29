from django.db import models
from django.utils import timezone
# Create your models here.
class ClasFormModel(models.Model):
    full_name = models.CharField(max_length=300,blank=True)
    email_id = models.CharField(max_length=300,blank=True)
    contact_number = models.CharField(max_length=300,blank=True)
    message = models.TextField(max_length=3000,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Contact Forn data"
        verbose_name = "Contact Form"