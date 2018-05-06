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

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def search_by_image_category(cls, search_term):
        pic = cls.objects.filter(name__icontains=search_term)
        return pic


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to='picfolder/')
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=500)
    image_location = models.ForeignKey(Location)
    image_category = models.ManyToManyField(Category)
    time_uploaded = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.image_name

    @classmethod
    def get_Image_by_category(cls, category):
        pic = cls.objects.filter(image_category=category).all()
        return pic

    @classmethod
    def get_Image_by_location(cls, location):
        pic = cls.objects.filter(image_location=location).all()
        return pic

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
