from django.test import TestCase
import datetime as dt
from .models import Location, Category, Image

# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='science')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category_method(self):
        self.category.save_category()
        category_object = Category.objects.all()
        self.assertTrue(len(category_object) > 0)

    def test_delete_category_method(self):
        self.category.save_category()
        category_object = Category.objects.all()
        self.category.delete_category()
        category_object = Category.objects.all()
        self.assertTrue(len(category_object) == 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(image='imageurl', image_name='camera', image_description='capturing device')

    def test_image_instance(self):
        self.assertTrue(isinstance(self.image, Image))


    def test_delete_image_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
        



