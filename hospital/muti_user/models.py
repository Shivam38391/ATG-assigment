from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db) #use existing database
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password,
            
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user




class CustomUser(AbstractBaseUser):
    DOCTOR = 1
    PATIENT = 2

    ROLE_CHOICE = (
        (DOCTOR, 'doctor'),
        (PATIENT, 'patient'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    state = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=12, blank=True)
    pincode = models.IntegerField(blank=True, null=True)
    line = models.CharField('line1',max_length=50,blank=True, null=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)


#authentication part of django custom user model
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    
    

class BlogPost(models.Model):
    
    categories = [
        ('Mental Health' , 'Mental Health' ),
        ('Heart Disease' , 'Heart Disease' ),
        ('Covid19' , 'Covid19' ),
        ('Immunization' , 'Immunization' ),
        
    ]
    
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/' , blank=True , default= 'defaultblog.png')
    category = models.CharField(choices=categories,max_length=50)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
