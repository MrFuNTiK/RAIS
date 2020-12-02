from django.db import models

class URLTable(models.Model):
    urladress = models.URLField(max_length=200)
    idurl = models.AutoField(primary_key=True)
    def __str__(self):
        return self.urladress

class WORDSTable(models.Model):
    idword = models.AutoField(primary_key=True)
    word = models.CharField(max_length=11)
    def __str__(self):
        return self.word

class COUNTTable(models.Model):
    idurl = models.ForeignKey(URLTable, on_delete=models.CASCADE)
    idword = models.ForeignKey(WORDSTable, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
