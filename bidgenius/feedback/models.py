from django.db import models

class FeesBack(models.Model):
    CHOICES = [('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')]
    email = models.EmailField()
    response = models.TextField()
    ratings = models.CharField(max_length=10, choices=CHOICES)
    feedback_date = models.DateTimeField(auto_now_add=True)