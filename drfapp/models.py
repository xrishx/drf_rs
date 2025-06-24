from django.db import models
from django.utils.text import slugify
from uuid import uuid4

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the book")
    # If fullpage content, always have public_id and slug
    public_id = models.UUIDField(default=uuid4, editable=False, unique=True, help_text="Unique identifier for the book")
    slug = models.SlugField(max_length=255, editable= False, unique=True, help_text="Slug for the book URL")
    author = models.ForeignKey('drfapp2.Author', related_name='Author', on_delete=models.CASCADE, help_text="Author(s) of the book")
    genre = models.CharField(max_length=100, help_text="Genre of the book")
    published_date = models.DateField(null=True, blank=True, help_text="Date when the book was published")    
    isbn = models.CharField(max_length=13, unique=True, help_text="ISBN number of the book")
    pages = models.IntegerField(null=True, blank=True, help_text="Number of pages in the book")
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True, help_text="Cover image of the book")
    # Always have created and updated timestamps
    created_date = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the book was created")
    updated_date = models.DateTimeField(auto_now=True, help_text="Timestamp when the book was last updated")

    def __str__(self):
        return self.title

    # Create SlugID from title and public_id if slug is not given
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.title)}-{str(self.public_id)[1:5]}-{str(self.public_id)[-1:-5]}'
        super().save(*args, **kwargs)

