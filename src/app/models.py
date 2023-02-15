from django.db import models


from tinymce.models import HTMLField

# Create your models here.

class Convention(models.Model):
    date_add = models.DateTimeField( auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField( auto_now=True, auto_now_add=False)
    publish = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Categorie(Convention):
    nom = models.CharField(max_length=50)
    libele = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categorie"    
        verbose_name_plural = "Categories" 
    
    def __str__(self):
        return self.nom
    
    
class Tag(Convention):
    nom = models.CharField(max_length=50)
    libele = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tag"    
        verbose_name_plural = "Tags" 
    
    def __str__(self):
        return self.nom
    


class Article(Convention):
    titre = models.CharField(max_length=50)
    libele = HTMLField()
    description = HTMLField()
    tag = models.ManyToManyField("app.Tag")
    picture = models.FileField(upload_to="img_article")
    picture1 = models.FileField(upload_to="img_article")
    Categorie = models.ForeignKey("app.Categorie", on_delete=models.SET_NULL, null = True)
    
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Article"
   
    def __str__(self):
       return self.titre
   
class About(Convention):
    titre = models.CharField(max_length=50)
    qui_suis_je = HTMLField()
    ma_vision = HTMLField()
    description = HTMLField()
    
    class Meta:
        verbose_name = "A propos de moi"
        verbose_name_plural = "A propos de moi"
    
    def __str__(self):
        return self.titre


class Social(Convention):
    nom = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    lien = models.URLField(max_length=200)
    
    class Meta:
        verbose_name = "réseau social"
        verbose_name_plural = "réseaux sociaux"
    
    def __str__(self):
        return self.nom
    

class Newsletter(Convention):
    email = models.EmailField(max_length=254)
    
    class Meta:
        verbose_name = "Abonnement"
        verbose_name_plural = "Abonnements"
    
    def __str__(self):
         return self.email


class Contact(Convention):
    nom = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    messages = models.TextField()
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    
    def __str__(self):
         return self.nom