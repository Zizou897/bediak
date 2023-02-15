from app.models import *



def get_articles(data=dict()):
    return Article.objects.filter(**data).order_by("-date_add")
