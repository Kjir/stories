from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Story(models.Model):
    description = models.CharField(max_length=200)
    final_estimate = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.description

class Evaluation(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    estimate = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return "Estimation by %s: %d" % (self.user, self.estimate)

    class Meta:
        unique_together = ('story', 'user',)
