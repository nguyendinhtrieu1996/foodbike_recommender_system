from django.db import models

class Similarity(models.Model):
    created = models.DateField()
    source = models.IntegerField()
    target = models.IntegerField()
    similarity = models.DecimalField(max_digits=8, decimal_places=7)

    class Meta:
        db_table = 'similarity'

    def __str__(self):
        return "[({} => {}) sim = {}]".format(self.source,
                                              self.target,
                                              self.similarity)


