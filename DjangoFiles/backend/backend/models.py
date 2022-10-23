from django.db import models
from ..TreeLossChart import Launchpad
import pandas as pd
# Create your models here.

class TreeLoss(models.Model):
    
    df = pd.read_csv('Tree cover loss in United States compared to other areas/treecover_loss_by_region__ha.csv')

    title = models.CharField(max_length=120)
    description = models.TextField()
    # TODO: take user input for chart - refer to forms.py
    # FIXME: import currently not working
    chart = Launchpad.TreeLossChart()
    
    def _str_(self):
        return self.title, self.description