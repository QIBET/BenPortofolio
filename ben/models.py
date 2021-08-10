from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.fields import DateField
from django.utils import timezone 
from django.dispatch import receiver




class Projects(models.Model):
    '''
    class to create instances of projects
    '''
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    project_name = models.CharField(max_length=30)
    description = models.TextField()
    livesite = models.URLField()
    image = cloudinary.models.CloudinaryField('image',null=True, blank=True)
    date_posted = models.DateField(default=timezone.now)
   

    def __str__(self):
        
        return self.project_name
    
    def save_project(self):
        '''
        method to save instances of projects
        '''
        self.save()

    def delete_project(self):
        '''
        method to delete instances of projects
        '''
        self.delete()

    @classmethod
    def get_projects(cls):
        '''
        method to return all projects
        '''
        all_projects = cls.objects.all()

        return all_projects

    @classmethod
    def search_by_project_name(cls,search_term):
        '''
        method to search and return project by name
        '''
        project = cls.objects.filter(project_name__icontains=search_term)
        return project