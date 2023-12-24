from django.db import models

# Create your models here.
class Quiz_Registration_Form(models.Model):
    Name = models.CharField(max_length=100)
    Contact = models.BigIntegerField()
    Mail = models.EmailField()

    class Meta:  
        db_table = "quiz_form"