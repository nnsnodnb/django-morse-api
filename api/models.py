from django.db import models
from datetime import datetime

class ReceiveSentence(models.Model):
    sentence = models.CharField(max_length = 100)
    receive_date = models.DateField(auto_now_add = True)
