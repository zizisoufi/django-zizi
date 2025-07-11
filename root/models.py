from django.db import models
from django.contrib.auth.models import User 
class pricing(models.Model):
    title = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    items = models.ManyToManyField("root.Item")  # فرض بر اینکه Item در همین فایل هست
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ و ساعت آخرین بروزرسانی

    def __str__(self):
        return self.title

class Item(models.Model):
    content = models.CharField(max_length=100)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    
    
    
class FrequentlyQuestion(models.Model):
        question = models.TextField()
        answer = models.TextField()
        status = models.BooleanField(default=True )
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)  # تاریخ و ساعت آخرین بروزرسانی

        def __str__(self):
            return self.question
class Skills(models.Model):
        title = models.CharField(max_length=100, default="skl")
        status = models.BooleanField(default=True )
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)  # تاریخ و ساعت آخرین بروزرسانی

        def __str__(self):
            return self.title
        
        
class Star(models.Model):
    count = models.PositiveIntegerField(default=3)

    def __str__(self):
        return str(self.count)
    
    def count_object(self):
        return range(self.count)

class Team(models.Model):
        image = models.ImageField(upload_to="profile", default="profile/default.jpg")
        name = models.ForeignKey(User, on_delete=models.CASCADE )
        description = models.TextField(default="test description")
        status = models.BooleanField(default=True )
        skills = models.ManyToManyField(Skills)
        stars = models.ForeignKey(Star, on_delete=models.DO_NOTHING)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)  # تاریخ و ساعت آخرین بروزرسانی

        def __str__(self):
            return self.name.username


class Leader(models.Model):
        image = models.ImageField(upload_to="profile", default="profile/default.jpg")
        name = models.ForeignKey(User, on_delete=models.CASCADE )
        description = models.TextField(default="test description")
        status = models.BooleanField(default=True )
        skills = models.ManyToManyField(Skills)
        twitter = models.CharField(max_length=255, default="#")
        facebook = models.CharField(max_length=255, default="#")
        instagram = models.CharField(max_length=255, default="#")
        linkdin = models.CharField(max_length=255, default="#")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)  # تاریخ و ساعت آخرین بروزرسانی

        def __str__(self):
            return self.name.username
