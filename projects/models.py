from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=100)
    # Estimated time
    estimated_time = models.IntegerField()
    # Estimated price
    estimated_price = models.IntegerField()
    # Objective of the project
    objective = models.TextField()
    # What I've learned from the project
    learned = models.TextField()
    # Each project has 1 image attached
    image = models.ImageField(upload_to='static/images/projects/')
    # Explaining text of the project
    body = models.TextField()
    # Date of creation
    date = models.DateTimeField()

    github_link = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
