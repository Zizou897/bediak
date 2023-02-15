from django.shortcuts import render


from app.functions import *
# Create your views here.


def home(request):
    
    get_all_articles = get_articles({'publish':True})
    
    template_name = 'app/layout/index.html'
    context = {
        'get_all_articles': get_all_articles,
    }
    return render(request, template_name, context)


def blogDetail(request):
    
    template_name = 'app/layout/detail.html'
    context = {}
    return render(request, template_name, context)


def blog(request):
    
    template_name = 'app/layout/blog.html'
    context = {}
    return render(request, template_name, context)


def contact(request):
    
    template_name = 'app/layout/contact.html'
    context = {}
    return render(request, template_name, context)



def about(request):
    
    template_name = 'app/layout/about.html'
    context = {}
    return render(request, template_name, context)