from django.db import models
from django.contrib.auth.models import User




#categories of products
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'



class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    director = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/movie/')

    def __str__(self):
        return self.title
    
# RATE_CHOICES = [
#     (1, '1 - Trash'),
#     (2, '2 - Horrible'),
#     (3, '3 - Terrible'),
#     (4, '4 - Bad'),
#     (5, '5 - Ok'),
#     (6, '6 - Watchable'),
#     (7, '7 - Good'),
#     (8, '8 - Very Good'),
#     (9, '9 - Perfect'),
#     (10, '10 - Master Piece'),
# ]

# class Review(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # date = models.DateTimeField(auto_now_add=True)
#     comment = models.TextField(max_length=1000)
#     rating = models.FloatField(default=0)
#     # likes = models.PositiveIntegerField(default=0)
#     # unlikes = models.PositiveIntegerField(default=0)
    
#     def __str__(self):
#         return self.user.username





class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
    
    
    # rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    # comment = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.user.username}'s review for {self.movie.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username
