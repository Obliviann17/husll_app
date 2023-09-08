from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    main_price = models.CharField(max_length=10)
    discount_price = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=250)
    photo = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    available = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_page', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = 'Товари'
        verbose_name_plural = 'Товари'
        ordering = ['name', ]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категорії'
        verbose_name_plural = 'Категорії'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Необхідно ввести email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = PhoneNumberField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    region = models.CharField(max_length=100, default='', verbose_name='Region')
    city = models.CharField(max_length=100, default='', verbose_name='City')
    new_post = models.CharField(max_length=100, default='', verbose_name='New Post')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Користувачі'
        verbose_name_plural = 'Користувачі'

class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
