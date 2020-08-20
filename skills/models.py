from django.db import models


class SkillCategory(models.Model):
    name = models.CharField(max_length=50)
    feature_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.name, self.value)
