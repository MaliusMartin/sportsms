from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone
from django.contrib.auth.models  import User
# Create your models here.

class Status(models.TextChoices):
    DRAFT = 'DF', 'Draft'
    PUBLISHED = 'PUB', 'Published'
    
class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()\
                    .filter(status=Status.PUBLISHED)  

class Sport(models.Model):
    sports = models.CharField(max_length=200)
    subsports = models.TextField()
    image = models.ImageField(upload_to='sport_icons', null=True, blank=True)
    description = models.TextField(blank=True, null=True)  # Description for the sport
    
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
    
# class Post(models.Model):
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250, unique_for_date='publish')
#     summary = models.CharField(max_length=500, blank=True)  # New field for a short preview
#     body = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=5, choices=Status.choices, default=Status.DRAFT)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
#     image = models.ImageField(upload_to='post_images/', blank=True, null=True)
#     views = models.PositiveIntegerField(default=0)  # Track number of views
#     featured = models.BooleanField(default=False)  # Mark special posts
#     published = PublishedManager()
#     # tags = TaggableManager()

#     class Meta:
#         ordering = ['-publish']
#         indexes = [models.Index(fields=['-publish'])]

#     def __str__(self):
#         return self.title
    
class Author(models.Model):
    Fname = models.CharField(max_length=200, null=False)
    Sname = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=254, validators=[EmailValidator(message="Invalid email address.")])
    bio = models.TextField(blank=True, null=True)  # New field for author bio
    profile_picture = models.ImageField(upload_to='authors/', blank=True, null=True)  # Author profile picture

    def __str__(self):
        return f"{self.Fname.capitalize()} {self.Sname.capitalize()}"

# class Author(models.Model):
#     Fname = models.CharField(max_length=200, null=False)
#     Sname = models.CharField(max_length=200, null=False)
#     email = models.EmailField(("email"), max_length=254, validators=[EmailValidator(message="Invalid email address.")])
    
#     def __str__(self) -> str:
#         return f"{self.Fname.capitalize()} {self.Sname.capitalize()} ...contact {self.email}"
    
    
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
 
      
    def __str__(self):
        return   f"{self.headline[:50]}...."
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    likes = models.PositiveIntegerField(default=0)  # Track likes on comments
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')  # Allow replies

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

# class Sport(models.Model):
#     sports = models.CharField(max_length=200)
#     subsports = models.TextField()
#     image = models.ImageField(upload_to='sport_icons', null=True, blank=True)
#     description = models.TextField(blank=True, null=True)  # Description for the sport

#     def __str__(self):
#         return self.sports

# class Detail(models.Model):
#     Sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
#     Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
#     Post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     Author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=250)
#     text = models.TextField()
#     image = models.ImageField(upload_to='detail_images', null=True, blank=True)
#     image2 = models.ImageField(upload_to='detail_images', null=True, blank=True)  # Renamed for clarity
#     image3 = models.ImageField(upload_to='detail_images', null=True, blank=True)  # Renamed for clarity
#     video = models.URLField(blank=True, null=True)  # New field for embedding videos
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.headline[:50]}..."
