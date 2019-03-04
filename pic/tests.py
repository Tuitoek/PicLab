from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTestClass(TestCase):

    #Set up method
    def setUp(self):
      self.mombasa=Location(image_location='Mombasa')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mombasa,Location))

    # Testing save method
    def test_save_location(self):
        self.mombasa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    # Testing delete method
    def test_delete_location(self):
        self.mombasa.save_location()
        self.mombasa.delete_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==0)

class ImageTestClass(TestCase):

    """
    Testclass for testing the image class
    """

    def setUp(self):
        self.new_location=Location(name='Mombasa')
        self.new_location.save_location()

        self.new_category=Category(name='Food')
        self.new_category.save_category()
        self.new_image = Image(image_name='Fab',image_location=self.new_location,image_category=self.new_category)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    # Testing Save Method
    def test_save_method(self):
        self.new_image.save_image()
        editors = Editor.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.Image.delete_image()
        self.assertEqual(len(),1)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_get_imagesby_location(self):
        images_by_location = Category.get_imagesby_location()
        self.assertTrue(len(images_by_location) == 0)




class CategoryTestClass(TestCase):
    '''
    Testclass for testing if the category class is working
    '''
    # Set up method
    def setUp(self):
        self.food = Category(image_category='Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))

    def test_save_category(self):
        self.food.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.food.save_category()
        self.food.delete_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)==0)


    def test_get_imagesby_category(self):
        images_by_category = Category.get_imagesby_category()
        self.assertTrue(len(images_by_category) == 0)
