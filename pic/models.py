from django.db import models

#Created models
class Location(models.Model):
    image_location= models.CharField(max_length=600)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.save(len(Location),2)

    @classmethod
    def get_imagesby_location(cls):
        images = cls.objects.filter(image_location)
        return news

    @classmethod
    def search_by_location(cls,search_term):
        images = cls.objects.filter(image_location=search_term)
        return images



class Category(models.Model):
    image_category=models.CharField(max_length=100)
    @classmethod
    def get_imagesby_category(cls):
        images = cls.objects.filter(image_category)
        return news

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category=search_term)
        return images

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.save(len(Category),2)

    @classmethod
    def get_imagesby_category(cls):
        images = cls.objects.filter(image_category)
        return news

class Image(models.Model):
    image_path = models.ImageField(upload_to ='images/')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length=30)
    image_location = models.ForeignKey(Location)
    image_category= models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.save(len(Image),2)

    @classmethod
    def get_image_by_id(id):
        idimage = Image.objects.filter(id)
        return idimage

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category=search_term)
        return images

    @classmethod
    def filter_by_location(location):
        locage = location.objects.filter(image_location)
