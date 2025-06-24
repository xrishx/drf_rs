from django.db import models
from uuid import uuid4
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255, help_text="First name of the author")
    last_name = models.CharField(max_length=255, help_text="Last name of the author")
    public_id = models.UUIDField(default=uuid4, editable=False, unique=True, help_text="Unique identifier for the author")
    slug = models.SlugField(max_length=255, editable= False, unique=True, help_text="Slug for the author URL")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Date of Birth")
    date_of_death = models.DateField(null=True, blank=True, help_text="Date of Death")
    awards = models.CharField(max_length=255, null=True, blank=True, help_text="Awards won by the author")
    created_date = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the author was created")
    updated_date = models.DateTimeField(auto_now=True, help_text="Timestamp when the author was last updated")


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.first_name)}-{str(self.public_id)[1:5]}-{str(self.public_id)[-1:-5]}'
        super().save(*args, **kwargs)
