from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField()

    def __str__(self):
        return self.title

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company}"

class About(models.Model):
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50)
    languages_known = models.CharField(max_length=100)
    dob = models.DateField(verbose_name="Date of Birth")
    father_name = models.CharField(max_length=100)
    education = models.CharField(max_length=255)
    interests = models.TextField()
    goals = models.TextField()

    def __str__(self):
        return f"{self.father_name}'s Child - {self.gender}"
    

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Contact - {self.email}"

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"