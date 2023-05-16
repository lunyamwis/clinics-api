from django.db import models
from api.models import BaseModel
# Create your models here.

class Role(BaseModel):
    """
    Name: CharField 
    """
    name = models.CharField(max_length=255)