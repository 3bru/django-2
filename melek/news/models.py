from django.db import models

# Create your models here.

class NewsItem(models.Model):
	"""docstring fos NeewsItem"""
	title=models.CharField(max_length=255)
	date_creatiton=models.DateTimeField(auto_now_add=True)
	date_publish=models.DateTimeField(blank=True)
	content=models.TextField()
	