from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    join_date = models.DateTimeField('Join Date')


    def __str__(self):
        return self.user_name
        # adding a custom database

class Post(models.Model):
    user_id = models.ForeignKey(User)
    post_name = models.CharField(max_length=30)
    post_text = models.CharField(max_length=200)
    post_tag = models.IntegerField()
    post_catid = models.IntegerField(default=0)
    post_votes = models.IntegerField()

    def __str__(self):
        return self.post_name

