from django.db import models

# Create your models here.
class OurUrl(models.Model):
    id = models.AutoField(primary_key=True)
    site = models.TextField(help_text="Imput URL's here")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.site