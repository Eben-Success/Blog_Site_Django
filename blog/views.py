from django.views.generic import( 
    ListView, 
DetailView, 
CreateView, 
UpdateView,
DeleteView
)
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.




def home(request):
    context = {
    'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    paginate_by = 5
    model = Post
    template_name = 'blog/home.html' #<app> / <model> _ <viewtype>.
    context_object_name = 'posts'
    ordering = ['-date_posted']

class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user_post.html'
    paginate_by: int = 5

    #filter users with particular post
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    #override form valid method

    def form_valid(self, form):
        # the form you are submit is by the current user
        #the .pk is a new added feature.
        form.instance.author = self.request.user
        return super().form_valid(form)
        

#LoginRequiredMixin ensures the user logins before updating post.
# UserPassesTestMixin ensures user do not update other people's blog
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    

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