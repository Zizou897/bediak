from django.contrib import admin
from  django.utils.safestring import mark_safe

from .models import *
# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'libele', 'publish')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nom', 'libele', 'publish')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'titre',  'libele', 'publish')
    
    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.picture.url}" style ="height:100px; width:200px>"')



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('titre', 'publish')



@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('nom','icon', 'lien', 'publish')
    


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'publish')



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'messages', 'publish')
    