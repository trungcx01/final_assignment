from django.db import models

class ClothesCategory(models.Model):
    name = models.CharField(max_length=255, unique= True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'c_categories'
        ordering = ['-created_at']
        # verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Clothes(models.Model):
    id = models.CharField(max_length=10, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    images = models.ImageField(upload_to='images/')
    description = models.TextField()
    categories = models.ManyToManyField(ClothesCategory)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clothes'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            prefix = 'C'
            last_clothes = Clothes.objects.all().order_by('id').last()
            if last_clothes:
                last_id = last_clothes.id[1:]
                new_id = str(int(last_id) + 1).zfill(4)
            else:
                new_id = '0001'
            self.id = prefix + new_id
        super(Clothes, self).save(*args, **kwargs)
