from django.db import models

class Similarity(models.Model):
    created = models.DateField()
    source = models.CharField(max_length=16, db_index=True)
    target = models.CharField(max_length=16)
    similarity = models.FloatField()

    class Meta:
        db_table = 'similarity'

    def __str__(self):
        return "[({} => {}) sim = {}]".format(self.source,
                                              self.target,
                                              self.similarity)


