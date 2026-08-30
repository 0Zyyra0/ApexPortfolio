from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from Hamilton.forms import NameForm , contactForm
from blog.models import Post, category as Category


def blog_view(request, cat_name=None, author_username=None):

    posts = Post.objects.filter(status=1)

    if cat_name:
        posts = posts.filter(category__name__iexact=cat_name)

    if author_username:
        posts = posts.filter(author__username=author_username)

    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'page_obj': page_obj,
    }

    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):

    post = get_object_or_404(
        Post,
        pk=pid,
        status=1
    )

    context = {
        'post': post
    }

    return render(request, 'blog/blog-single.html', context)


def test(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            return HttpResponse('done')
        else:
            return HttpResponse('FUCK YOU')
    form = contactForm()  
    
    return render(request, 'test.html')

def blog_category(request, cat_name):

    posts = Post.objects.filter(
        category__name__iexact=cat_name,
        status=1
    )

    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'page_obj': page_obj,
    }

    return render(request, 'blog/blog-home.html', context)


def blog_search(request):

    query = request.GET.get('s')

    posts = Post.objects.filter(status=1)

    if query:
        posts = posts.filter(title__icontains=query)

    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'blog/blog-home.html', context)