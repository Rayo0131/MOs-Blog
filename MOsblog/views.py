from django.shortcuts import render, get_object_or_404
from .models import Article, Category

# Create your views here.

def Homepage(request):
    stories = Article.objects.filter(is_published=True).order_by('-pub_date')
    categories = Category.objects.all()
    latest_news = Article.objects.filter(is_published=True).order_by('-pub_date')[:5]
    big_news = Article.objects.filter(category__name="Breaking News", is_published=True).order_by('-pub_date')[:1]
    top_news = Article.objects.filter(category__name= "sport", is_published=True).order_by('-pub_date')[:4]
    carousel_slider = Article.objects.filter(category__name= "Weddings", is_published=True).order_by('-pub_date')[:8]
    carousel_news = Article.objects.filter(category__name= "Weddings", is_published=True).order_by('-pub_date')[:5]
    slider_news = Article.objects.filter(category__name= "Weddings", is_published=True).order_by('-pub_date')[:2]
    return render(request, 'homepage.html', {'stories': stories, 'categories': categories, 'latest_news': latest_news, 'big_news': big_news, 'top_news': top_news, 'carousel_slider': carousel_slider, 'carousel_news': carousel_news, 'slider_news': slider_news })


def article_details (request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True )
    categories = Category.objects.all()
    return render(request, 'article_details.html',{'article':article, 'categories':categories})


def category (request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category).order_by('-pub_date')
    categories = Category.objects.all()
    return render(request, 'category.html', {'category':category, 'articles':articles, 'categories':categories})