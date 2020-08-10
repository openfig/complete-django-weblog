from django.views.generic import ListView,DetailView
from account.models import User
from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404

# from django.http import HttpResponse
from .models import Article,Category

# Create your views here.

# def home(request,page=1):
#     articles_list =Article.objects.filter(status='p').order_by('-publish')
#     paginator = Paginator(articles_list,4)
#     articles = paginator.get_page(page)
#     context = {
#         'articles':articles,
#     }
#     return render(request,'blog/home.html',context)

class ArticleLIst(ListView):
    # model = Article
    # template_name = 'blog/home.html'
    context_object_name = 'articles'
    queryset = Article.objects.published()
    paginate_by = 4

# def detail(request,slug):
#     context = {
#         'article':get_object_or_404(Article,slug=slug,status='p')
#     }
#     return render(request,'blog/detail.html',context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article,slug=slug,status='p')

# def category(request,slug,page=1):
#     category = get_object_or_404(Category,slug=slug,status=True)
#     articles_list = category.articles.all()
#     paginator = Paginator(articles_list,4)
#     articles = paginator.get_page(page)
#     context = {
#         'category': category,
#         'articles':articles,
#     }
#     return render(request,'blog/category.html',context)

class CategoryList(ListView):

    paginate_by = 4
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        global category
        category = get_object_or_404(Category,slug=slug,status=True)
        return category.articles.published()
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

class AuthorList(ListView):

    paginate_by = 4
    template_name = 'blog/author_list.html'

    def get_queryset(self):
        username = self.kwargs.get('username')
        global author
        author = get_object_or_404(User,username=username)
        return author.articles.published()
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context