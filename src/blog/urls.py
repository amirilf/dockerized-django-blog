from django.urls import path
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    path('',TemplateView.as_view(template_name='blog.html'),name='index'),
    path('article',TemplateView.as_view(template_name='article.html'),name='article')

]
