from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='category/photos')
    
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Product(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_new = models.BooleanField(default=False)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title



class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images')
    
    class Meta:
        verbose_name_plural = 'Product Images'
        verbose_name = 'Product Image'
        
    def __str__(self):
        return f'Image of {self.product.title}'
    