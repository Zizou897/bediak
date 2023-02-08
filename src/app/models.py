from django.db import models


from tinymce.models import HTMLField

# Create your models here.

class Convention(models.Model):
    date_add = models.DateTimeField( auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField( auto_now=True, auto_now_add=False)
    publish = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Article(Convention):
    titre = models.CharField(max_length=50)
    libele = HTMLField()
    description = HTMLField()
    picture = models.FileField(upload_to="img_article")
    picture1 = models.FileField(upload_to="img_article")
   
    def __str__(self):
       return self.titre
   