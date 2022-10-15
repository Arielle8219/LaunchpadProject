from django.db import models
from Launchpad import *
# Create your models here.

class TreeLoss(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    #TODO: take user input for chart
    chart = TreeLossChart()

    def _str_(self):
        return self.title, self.description, self.chart