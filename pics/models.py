from django.db import models

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=30)
    
    @classmethod
    def search_by_image_location(cls, search_term):
        pic = cls.objects.filter(location__icontains=search_term)
        return pic

    def __str__(self):
        return self.location

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    @classmethod
    def search_by_image_category(cls, search_term):
        pic = cls.objects.filter(name__icontains=search_term)
        return pic
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='picfolder/')
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=30)
    image_location = models.ForeignKey(Location)
    image_category = models.ManyToManyField(Category)

    @classmethod
    def get_Image_by_category(cls, category):
        pic = cls.objects.filter(image_category=category).all()
        return pic

    @classmethod
    def get_Image_by_location(cls, location):
        pic = cls.objects.filter(image_location=location).all()
        return pic

    def __str__(self):
        return self.image_name
