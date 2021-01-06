#Blog
from django.shortcuts import render
from blog.models import BlogPost

def index(request):
    return render(request, 'blog/index.html')

def blog_entries(request):
    entries = BlogPost.objects.order_by('-created_on')
    context = {"entries": entries}
    return render(request, "blog/blog_entries.html", context)

def blog_entry(request, blog_id):    
    entry = BlogPost.objects.get(id=blog_id)
    context = {'entry': entry}
    return render(request, 'blog/blog_entry.html', context)
