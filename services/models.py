from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Specials(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(default="test")
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name



class Services(models.Model):
    image = models.ImageField(upload_to="service",default="services.jpg")
    stitle = models.CharField(max_length=200)
    content = models.TextField()
    ltitle = models.CharField(max_length=200) 
    desc1 = models.TextField()
    desc2 = models.TextField()
    category = models.ManyToManyField(Category)
    specials = models.ManyToManyField(Specials)
    status = models.BooleanField(default=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ و ساعت آخرین بروزرسانی

    def __str__(self):
        return self.stitle
    