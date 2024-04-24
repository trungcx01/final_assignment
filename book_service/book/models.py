from django.db import models

class BookCategory(models.Model):
    name = models.CharField(max_length=255, unique= True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'b_categories'
        ordering = ['-created_at']
        # verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    mail = models.EmailField()

    class Meta:
        db_table = 'author'
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    mail = models.EmailField()

    class Meta:
        db_table = 'publisher'

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.CharField(max_length=10, primary_key=True, editable=False)
    title = models.CharField(max_length=50, unique=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()
    images = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField()
    language = models.CharField(max_length=30)
    categories = models.ManyToManyField(BookCategory)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            prefix = 'B'
            last_book = Book.objects.all().order_by('id').last()
            if last_book:
                last_id = last_book.id[1:]
                new_id = str(int(last_id) + 1).zfill(4)
            else:
                new_id = '0001'
            self.id = prefix + new_id
        super(Book, self).save(*args, **kwargs)
