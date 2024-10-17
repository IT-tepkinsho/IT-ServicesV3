from django.db import models

class RepairType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RepairTopic(models.Model):
    name = models.CharField(max_length=100)
    repair_type = models.ForeignKey(RepairType, related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
