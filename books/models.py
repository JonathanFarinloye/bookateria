from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    downloads = models.IntegerField(default=0, editable=False)
    upload_date = models.DateTimeField()
    size = models.FloatField(null=True)
    image = models.ImageField(upload_to='images/')
    pdf = models.FileField(upload_to='file/')
    uploader = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255)

    def save(self, *args, **kwargs):
        self.slug = self.slug[:100]
        self.slug = slugify(self.title)
        return super(Books, self).save(*args, **kwargs)

    def megabytes(self):
        self.size = self.pdf.size
        if self.size < 1024:
            fsize = self.size
            message = str(fsize) + ' Bytes'
        elif self.size < 1048576:
            fsize = round(self.size/1024, 2)
            message = str(fsize) + ' Kb'
        else:
            fsize = round(self.size/1048576, 2)
            message = str(fsize) + ' Mb'
        return message

    def summary(self):
        return self.description[:100]

    def date(self):
        return self.upload_date.strftime('%b %e %Y')
    '%m %Y %-d'

    def __str__(self):
        return self.title


