from django.db import models
from django.contrib.auth.models import User
from random import sample
import string


class CodeGenerate(models.Model):
    code = models.CharField(max_length=255, blank=True, unique=True)
    
    @staticmethod
    def generate_code():
        return ''.join(sample(string.ascii_letters + string.digits, 15)) 
    
    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                code = self.generate_code()
                if not self.__class__.objects.filter(code=code).count():
                    self.code = code
                    break
        super(CodeGenerate,self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Company(CodeGenerate):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self):
        return f'{self.name}, {self.description}, {self.phone}, {self.website}'


class Service(CodeGenerate):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Client(CodeGenerate):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)

    
    def __str__(self):
        return self.name

    @property
    def projects(self):
        return Project.objects.filter(client=self)


class Project(CodeGenerate):
    name = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('PLANNING', 'Planning'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')])

    def __str__(self):
        return self.name


class Contact(CodeGenerate):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    text = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact Request from {self.name}'


class Employee(CodeGenerate):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    hire_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Role(CodeGenerate):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Assignment(CodeGenerate):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.employee} - {self.project}'


class Testimonial(CodeGenerate):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    feedback = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'Testimonial by {self.client}'


class BlogPost(CodeGenerate):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Partner(CodeGenerate):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partner_logos/')
    website_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class SocialLinkEmployee(CodeGenerate):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()


    def __str__(self):
        return f'{self.employee.first_name} - {self.name}'


class SocialLink(CodeGenerate):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

