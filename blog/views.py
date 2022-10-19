from django.shortcuts import render

posts = [
{
'author':'CoreyMS',
'title': 'Blog Post 1',
'content': 'First Post Content',
'date_posted': 'August 27, 2022'
},
{
    'author':'Success',
    'title': 'Blog Post 2',
    'content': 'Second Post Content',
    'date_posted': 'August 29, 2022'
},
]

# Create your views here.
def home(request):
    context = {
    'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})