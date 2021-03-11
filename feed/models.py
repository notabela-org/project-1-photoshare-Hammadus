from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
#
#		'author':'Hammadus',
#		'comments':'wow, so cool man',
#		'imageurl':'https://mdbootstrap.com/img/new/standard/nature/184.jpg',
#		'caption':'mountaints',
#		'dateposted':'March 7, 2021'
#
class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	caption = models.TextField()
	dateposted = models.DateTimeField(default=timezone.now)
	imageurl = models.CharField(max_length=250)

	def __str__(self):
		return f'{self.author.username} Posted'


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	dateposted = models.DateTimeField(default=timezone.now)

	class Meta: 
		ordering = ('dateposted',) 

	def __str__(self): 
	    return 'Comment by {} on {}'.format(self.author, self.post) 




