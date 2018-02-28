from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=300)
    reddit_link = models.URLField(max_length=200, unique=True)
    user = models.CharField(max_length=200, blank=True)
    user_age = models.IntegerField(blank=True)

    USER_SEX_CHOICES = (
        (None, 'None'),
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    user_sex = models.CharField(max_length=20, blank=True, choices=USER_SEX_CHOICES, default=None)
    user_height = models.IntegerField(default=0)
    user_body_type_start = models.CharField(max_length=200, blank=True)
    user_body_type_end = models.CharField(max_length=200, blank=True)
    user_starting_weight = models.IntegerField(blank=True)
    user_ending_weight = models.IntegerField(blank=True)
    goals = models.CharField(max_length=100, blank=True)
    calories = models.IntegerField(blank=True)
    macro_protein = models.IntegerField(blank=True, null=True)
    macro_carb = models.IntegerField(blank=True, null=True)
    macro_fat = models.IntegerField(blank=True, null=True)
    period = models.FloatField(blank=True)
    tldr = models.TextField(max_length=1000)
    def __str__(self):
        return self.name

class Food(models.Model):
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Progress(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    link = models.URLField(max_length=200, unique=True)
    description = models.CharField(max_length=250, blank=True)