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
`post1 = Post(title='Blog 1', content='First Post Content!', author=user)`
`post1.save()`

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

<hr>
### On your local machine
>- Make .ssh folder
`mkdir -p ~/.ssh`

* Generate public/private rsa key pair
`ssh-keygen -b 4096`
<br>

`scp ~/.ssh/id-rsa.pub eben-success@198.***.***: ~/.ssh/authorized_keys`

<hr>
### Server Terminal

`ls  .ssh`

`sudo chmod 700 ~/.ssh/`

* Add permissions on all files
`sudo chmod 600 ~/.shh/*`

* Disallowing password logins
`sudo nano /etc/ssh/sshd-config`
1. Change PermitRootLogin    no.
2. PasswordAuthentication   no.

* Restart ssh service
`sudo systemctl restart sshd`

<hr>
### Stepping Up a filewall

`sudo apt-get install ufw`

`sudo ufw default allow outgoing`

`sudo ufw default deny incoming`

Allow ssh
`sudo ufw allow ssh`

Allow port
`sudo ufw allow 8000`

Enable port 8000
`sudo ufw enable`

View allowed ports
`sudo ufw status`

If using a virtual environment for django project, create requirement.txt file.

<hr>

* Activate virtual environment
`source ~/bin/activate`

`pip freeze`

`pip freeze > requirements.txt`

Copy recursively
`scp -r django-project eben-success@198.***.***:~/`

`sudo apt-get install python3-pip`
<br>

## Set up Virtual Environment on Server
`sudo apt-get install python3-venv`

`python 3 -m venv django_project/venv`

`cd django_project/`

`souce venv/bin/activate`












