from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name='home'),
    path('article/<slug:slug>/', views.article_details, name="article"),
    path('category/<slug:slug>/',views.category, name="category"),


]