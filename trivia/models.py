from django.db import models

class Question(models.Model):
   nick = models.CharField(max_length=55)
   question = models.CharField(max_length=255)
   answer = models.CharField(max_length=255)
   alternate = models.CharField(max_length=255, blank=True)

   def __unicode__(self):
      return self.question

