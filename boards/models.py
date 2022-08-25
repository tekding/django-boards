from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name   

class Standard(models.Model):
    # 定义标准类型，国标或者行标
    standard_category =(
        ('国标','GB/T'),
        ('行标','QC/T'),
    )
    stdcat = models.CharField(max_length=30,choices=standard_category) 
    # 定义标准号
    stdnum = models.IntegerField()
    # 定义标准年代号
    stdyear = models.DateField(auto_now=False, auto_now_add=False)
    # 定义标准名称
    stdname = models.CharField(max_length=50)
    # 定义标准起草人
    authors = models.ManyToManyField(Author,through='Standard_to_Author')


class Standard_to_Author(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE) 

# class Board(models.Model):
#     name = models.CharField(max_length=30,unique=True)
#     description = models.CharField(max_length=100)  
#     def __str__(self):
#         return self.name

    

# class Topic(models.Model):
#     subject = models.CharField(max_length=255)
#     last_updated = models.DateTimeField(auto_now_add=True)
#     board = models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
#     starter = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)

# class Post(models.Model):
#     message = models.TextField(max_length=4000)
#     topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(null=True)
#     created_by = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
#     updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE)


# Create your models here.
