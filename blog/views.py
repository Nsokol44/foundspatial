from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify

from .models import Blog
from .forms import BlogForm
from taggit.models import Tag


def blog_home(request):
    posts = Blog.objects.order_by('-datetime')
    context = {
        'posts':posts,
    }
    return render(request, 'bloghome.html', context)


def blog_view(request):
    posts = Blog.objects.order_by('-datetime')
    # Show most common tags
    common_tags = Blog.tags.most_common()[:4]
    form = BlogForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        # Without this next line the tags won't be saved.
        form.save_m2m()
    context = {
        'posts':posts,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'blogsearch.html', context)



def detail_view(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    context = {
        'post':post,
    }
    return render(request, 'detail.html', context)



def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Blog.tags.most_common()[:4]
    posts = Blog.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
    }
    return render(request, 'blogsearch.html', context)
