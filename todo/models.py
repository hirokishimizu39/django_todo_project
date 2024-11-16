from django.db import models

# Create your models here.
# Modelを継承
class TodoModel(models.Model):
  title = models.CharField(max_length=100)
  memo = models.TextField()

  def __str__(self):
    return self.title