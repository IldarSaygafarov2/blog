from django.shortcuts import render, redirect
from .models import Article, Category, CustomUser
from .forms import ArticleForm, LoginForm, CustomUserRegister
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': 'Главная страница'
    }

    return render(request, 'blog/index.html', context)


def category_list(request, pk):
    articles = Article.objects.filter(category_id=pk)
    context = {
        'articles': articles,
        'title': articles[0].category.title if articles else 'Нет рецептов в данной категории'
    }

    return render(request, 'blog/index.html', context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    article.watch += 1
    article.save()

    articles = Article.objects.all()


    context = {
        'title': article.title,
        'article': article,
        'articles': articles

    }

    return render(request, 'blog/article_detail.html', context)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():

            article = Article.objects.create(**form.cleaned_data)
            article.author = request.user
            article.save()
            return redirect('article_detail', article.pk)

    else:
        form = ArticleForm

    context = {
        'form': form,
        'title': 'Добавить свой рецепт'
    }
    return render(request, 'blog/article_form.html', context)


def profile(request, user_id):
    user = User.objects.get(pk=user_id)

    articles = Article.objects.filter(author=user)
    articles = articles.order_by('-created_at')

    context = {
        'title': f'Пользователь {user.username}',
        'articles': articles,
        'user': user
    }

    return render(request, 'blog/profile.html', context)


class ArticleList(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/index.html'
    extra_context = {
        'title': 'Главная страница'
    }

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleListByCategory(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['pk'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Категория: {category.title}'
        return context


class ArticleDetail(DetailView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Рецепт: {article.title}'
        articles = Article.objects.all()
        articles = articles.order_by('-created_at')[:4]
        context['articles'] = articles
        return context


class NewArticle(CreateView):
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    extra_context = {
        'title': 'Добавить свой рецепт'
    }


class SearchResults(ArticleList):
    def get_queryset(self):
        word = self.request.GET.get('q')
        articles = Article.objects.filter(
            Q(title__icontains=word) | Q(content__icontains=word) | Q(ingredients__icontains=word), is_published=True
        )
        return articles


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('index')
    context_object_name = 'article'


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    context = {
        'title': 'Авторизация пользователя',
        'form': form
    }
    return render(request, 'blog/login_form.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
       form = CustomUserRegister(data=request.POST, files=request.FILES)
       if form.is_valid():
           form.save()
           return redirect('login')

    else:
        form = register

    context = {
        'title': 'Авторизация пользователя',
        'form': form
    }
    return render(request, 'blog/register.html', context)
