# Project Documentation


### Django Query Commands
* python manage.py migrate
* python manage.py shell

<hr>
import the following:

from blog.models import Post<br>
from django.contrib.auth.models import User

### View all Users
User.objects.all()

### Get the first user
User.objects.all().first()

### Filter objects
User.objects.filter(username='eben-success') 
<br>
User.objects.filter(username='eben-success').first()

### User.id
user.id

### User Primary Key
user.pk

### View all Post
Post.objects.all()

### Add Post
post1 = Post(title='Blog 1', content='First Post Content!', author=user)
post1.save()

### Using post_set 
user.post_set.all()

