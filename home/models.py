from django.db import models
from django.utils.text import slugify 

# Create your models here.  

class Category(models.Model):
    CategoryName = models.CharField(max_length=255, null=False, unique=True)
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(blank=True,null=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.CategoryName}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.CategoryName)
        super().save(*args, **kwargs)


class Campaigns(models.Model):
    Name = models.CharField(max_length=255, null=False, unique=True)
    image = models.ImageField(upload_to="Campaigns")
    slug = models.SlugField(blank=True, null=True,unique=True, db_index=True)
    isActive = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.Name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name}"


class Product(models.Model):
    Name = models.CharField(max_length=255, null=False, unique=True)
    Price = models.IntegerField( null=True)
    image = models.ImageField(upload_to="products")
    SalePrice = models.IntegerField()
    Descriptions = models.TextField(max_length=1000, null=False)
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True,unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isPopularInMainPage = models.BooleanField(default=False)
    isSaleInMainPage = models.BooleanField(default=False)
    campaign = models.ForeignKey(Campaigns, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name}"


class Descriptions(models.Model):
    text = models.TextField(max_length=250, null=False)