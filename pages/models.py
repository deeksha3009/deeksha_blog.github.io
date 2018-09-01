from django.db import models

class Posts(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.published_date =models.DateTimeField(auto_now_add=True)
        self.save()

    def __str__(self):
        return self.title

class BlogPost(models.Model):
 	title=models.CharField(max_length=200)
 	body=models.TextField()
 	date_published=models.DateTimeField(auto_now_add=True)
 	def __str__(self):
 	 	return self.title
