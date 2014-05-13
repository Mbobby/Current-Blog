from django.db import models
from datetime import datetime

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	pub_date = models.DateTimeField(default = datetime.now())
	likes = models.IntegerField(default = 0)	

	#making function to handle the printing of obects
	def __unicode__(self):
		return self.title
