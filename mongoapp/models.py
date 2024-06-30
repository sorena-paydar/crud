from djongo import models


class MongoModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
