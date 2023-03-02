from django.db import models
import uuid
from users.models import Profile
class ProjectsModel(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True )
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True, null=True)
    featured_image = models.ImageField(blank=True, null=True, default='default.png')
    tags = models.ManyToManyField('Tags', blank=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote')
    )
    projects = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE)
    body = models.TextField(max_length=2000, blank=True, null=True)
    value = models.CharField(max_length=200,blank=True, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.value


class Tags(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.name