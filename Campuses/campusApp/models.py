from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    Name = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    #creates the model manager
    object = models.Manager()

    #displays the object output values in the form of a string
    def __str__(self):
        #returns the input value of the title and instructor name
        #Field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.Name}: {0.campus_id}'
        return display_campus.format(self)

    #removes the added "s" that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campuses"
