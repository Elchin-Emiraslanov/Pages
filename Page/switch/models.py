from django.db import models

# Create your models here.
class Card(models.Model):
    # card_pk = models.ForeignKey(  ,models.CASCADE)
    img_url = models.URLField(max_length=200,null=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    title = models.CharField(max_length=16,null=True, blank=True)
    descriptions = models.CharField(max_length=64, null=True,blank=True)


    def __str__(self) -> str:
        return f"{self.title}"

