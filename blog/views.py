from django.views.generic import( 
    ListView, 
DetailView, 
CreateView
)
from django.shortcuts import render
from .models import Post


# Create your views here.




def home(request):
    context = {
    'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app> / <model> _ <viewtype>.
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fileds = ['title', 'content']
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# TYPES OF VIEWS
# list_views
# detailed_views
# create_views
# update_views
# delete_views
# subscribe_views
# 