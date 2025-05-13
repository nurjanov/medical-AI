from django.db import models
from django.utils import timezone

class MedicalImage(models.Model):
    image = models.ImageField(upload_to='medical_images/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    result = models.TextField(blank=True, null=True)  # Здесь будет "анализ"

    def __str__(self):
        return f"Image {self.id}"
  
