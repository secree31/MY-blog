from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Posting(models.Model):
    judul = models.CharField(max_length=200)
    konten = RichTextUploadingField()
    image = models.ImageField(null=True, blank=True, upload_to='image')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
