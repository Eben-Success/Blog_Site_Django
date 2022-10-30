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

### All Posts
user.post_set.all()

### Create new Post
user.post_set.create(title='Blog 3', content='Third Post Content')

## Deploying Application on Linode Server
### Setting Server on Ubuntu Locally
* Set up ssh on local mahcine.
* Install apps on local machine.
` apt-get update && apt-get upgrade`

`hostnamectl set-hostname django-server` <br><br>
Check it : `hostname`

`nano /etc/hosts`
Add: 198.58.119.183     django-server
(ssh IP) to host file

* Add limited user
`adduser eben-success`
password: *******

* Give new user admin priviledges
`adduser eben-success sudo`

* Log in into server
`ssh eben-success@198.***.***`

>- Make .ssh folder
`mkdir -p ~/.ssh`

* Generate public/private rsa key pair
`ssh-keygen -b 4096`
<br>

`scp ~/.ssh/id-rsa.pub eben-success@198.***.***: ~/.ssh/authorized_keys`










