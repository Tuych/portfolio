from django.db import models
from datetime import date


class AboutMe(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    birthday = models.DateField(blank=False, null=False)
    city = models.CharField(max_length=50, null=True, blank=True)
    degree = models.CharField(max_length=50, blank=True, null=True)  # degree daraja
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    git_hub_url = models.URLField(null=True, blank=True)
    leet_code_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.first_name

    @staticmethod
    def age():
        today = date.today()
        age = today.year - 2000
        return age


class Skills(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    level_of_knowledge = models.SmallIntegerField(default=0, )  # bilish darajasi skillarni
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    category = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    client = models.CharField(max_length=50, default='Portfolio project')
    project_date = models.DateField(blank=True, null=True)
    project_url = models.URLField(blank=False, null=False)
    image_title = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    image_main = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    view_portfolio_numbers = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-view_portfolio_numbers']


class Rezume(models.Model):
    edu_or_job = models.CharField(max_length=100,  blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    link_for_name = models.URLField(blank=True, null=True)
    block_pdf = models.FileField(upload_to='my_pdf_file/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
