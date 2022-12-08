from django.db import models

# Create your models here.

class Musician(models.Model):
    # id = models.AutoField(primary_key=True) //it wwill work autometically
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

    # video 8.1 name changing
    # class Meta:
    #   db_table = "Musician"

      # to check output data
    def __str__(self):
     return self.first_name + " " + self.last_name + self.instrument    


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()

    # creating tuple for choices
    rating = (
      (1, "worst"),
      (2, "bad"),
      (3, "moderate"),
      (4, "good"),
      (5, "excellent"),
    )

    num_starts = models.IntegerField(choices=rating)

    # class Meta:
    #   db_table = "Album"

    def __str__(self):
      return self.name +  ", Rating:" + str(self.num_starts)
