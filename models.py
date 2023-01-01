from django.db import models

class HighScore(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=15)
    score = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return "%s %d" % (self.name, self.score)
