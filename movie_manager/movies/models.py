from django.db import models

# Create your models here.
class CensorInfo(models.Model):
    rating = models.CharField(max_length=10,null=True)
    certified_by = models.CharField(max_length=200,null=True)
    def __str__(self):        
        return self.certified_by        
    

class DirectorInfo(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):  
        return self.name
    
class actorInfo(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class MovieInfo(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    year = models.IntegerField(null=True)
    success = models.BooleanField()
    img_name = models.ImageField(upload_to='images/', null=True, blank=True)

    censor_info = models.OneToOneField(CensorInfo, 
                                       on_delete=models.SET_NULL, 
                                       related_name='movie', 
                                       null=True)

    director_by = models.ForeignKey(DirectorInfo, 
                                    on_delete=models.CASCADE, 
                                    related_name='movies_directed', 
                                    null=True)

    actors = models.ManyToManyField(actorInfo, 
                                    related_name='movies_acted_in')
    
    def __str__(self):
        return self.title