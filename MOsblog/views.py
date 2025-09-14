from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def Homepage(request):
    stories = Article.objects.filter(is_published=True).order_by('-pub_date')
    categories = Category.objects.all()
    latest_news = Article.objects.filter(is_published=True).order_by('-pub_date')[:5]
    big_news = Article.objects.filter(category__name="Breaking News", is_published=True).order_by('-pub_date')[:1]
    top_news = Article.objects.filter(category__name="Sport", is_published=True).order_by('-pub_date')[:4]
    carousel_slider = Article.objects.filter(category__name="Weddings", is_published=True).order_by('-pub_date')[:8]
    carousel_news = Article.objects.filter(category__name="Weddings", is_published=True).order_by('-pub_date')[:5]
    slider_news = Article.objects.filter(category__name="Weddings", is_published=True).order_by('-pub_date')[:2]
    return render(request, 'homepage.html', {
        'stories': stories,
        'categories': categories,
        'latest_news': latest_news,
        'big_news': big_news,
        'top_news': top_news,
        'carousel_slider': carousel_slider,
        'carousel_news': carousel_news,
        'slider_news': slider_news
    })

def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    related_stories = (
        Article.objects.filter(category=article.category)
        .exclude(slug=slug)
        .order_by('-pub_date')[:5]
    )
    categories = Category.objects.all()
    comments = article.comments.order_by('-pub_date')
    comment_form = CommentForm()
    return render(request, 'article_details.html', {
        'article': article,
        'categories': categories,
        'comments': comments,
        'comment_form': comment_form,
        'related_stories': related_stories
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category, is_published=True).order_by('-pub_date')
    categories = Category.objects.all()
    return render(request, 'category.html', {
        'category': category,
        'articles': articles,
        'categories': categories
    })

def post_comment(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user if request.user.is_authenticated else None
            comment.is_approved = True
            comment.save()
            return redirect('article', slug=article.slug)
    return redirect('article', slug=article.slug)

def About(request):
    return render(request, 'about.html')

def Categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def Contact(request):
    return render(request, 'contact.html')

def Privacy(request):
    return render(request, 'privacy.html')

def Terms(request):
    return render(request, 'terms.html')