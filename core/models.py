from django.db import models
from django.core.validators import EmailValidator

# Create your models here.

class Sport(models.Model):
    sports = models.CharField(max_length=200)
    subsports = models.TextField()
    image = models.ImageField(upload_to='sport_icons', null=True, blank=True)
    
    def __str__(self) -> str:
        # return super().__str__()
        return self.sports
    

class Category(models.Model):
    Categories = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.Categories
    
    
class Post(models.Model):
    article = models.CharField( max_length=200)
    
    def __str__(self) -> str:
        return self.article
    
class Author(models.Model):
    Fname = models.CharField(max_length=200, null=False)
    Sname = models.CharField(max_length=200, null=False)
    email = models.EmailField(("email"), max_length=254, validators=[EmailValidator(message="Invalid email address.")])
    
    def __str__(self) -> str:
        return f"{self.Fname.capitalize()} {self.Sname.capitalize()} ...contact {self.email}"
    
    
class Detail(models.Model):
    Sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=False)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    headline = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to='detail_images', null=True, blank=True)  # Add the image field
    image2 = models.ImageField(upload_to='detail_images', null=True, blank=True)  # Add the image field
    image3 = models.ImageField(upload_to='detail_images', null=True, blank=True)  # Add the image field
    date_added = models.DateTimeField(auto_now_add=True)
    # images = models.ManyToManyField('Image', blank=True)
    # authors = models.ManyToManyField(Author)
    # date_mod  = models.DateTimeField(auto_now_add=True)
    # number_of_comments = models.IntegerField()
    # number_of_pingbacks =models.IntegerField()
    # rating = models.IntegerField()
      
    def __str__(self):
        return   f"{self.headline[:50]}...."
    


