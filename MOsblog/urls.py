from django.urls import path
from . import views
from .views import Homepage, article_details, category, post_comment

urlpatterns = [
    path('', views.Homepage, name='home'),
    path('article/<slug:slug>/', views.article_details, name="article"),
    path('category/<slug:slug>/',views.category, name="category"),
    path('article/<slug:slug>/comment/', views.post_comment, name='post_comment'),

    path('About', views.About,name='about'),
    path('Categories', views.Categories,name='categories'),
    path('Contact', views.Contact,name='contact'),
    path('privacy', views.Privacy,name='privacy'),
    path('terms', views.Terms,name='terms'),


]