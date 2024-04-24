from django.db import models

class MobileCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique= True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'm_categories'
        ordering = ['-created_at']
        # verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Mobile(models.Model):
    id = models.CharField(max_length=10, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='images/')
    storage = models.IntegerField()
    description = models.TextField()
    categories = models.ManyToManyField(MobileCategory)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mobiles'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            prefix = 'M'
            last_mobile = Mobile.objects.all().order_by('id').last()
            if last_mobile:
                last_id = last_mobile.id[1:]
                new_id = str(int(last_id) + 1).zfill(4)
            else:
                new_id = '0001'
            self.id = prefix + new_id
        super(Mobile, self).save(*args, **kwargs)