from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class SocialLink(models.Model):
    platform = models.CharField(max_length=100)
    url = models.URLField()
    icon_class = models.CharField(max_length=100, help_text="Bootstrap icon class, e.g., 'bi bi-twitter-x'")

    def __str__(self):
        return self.platform

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    detail = models.TextField(default=1)
    pic = models.ImageField(upload_to='image/', height_field=None, width_field=None, max_length=None) 
    



class About(models.Model):
    about_pics = models.ImageField(upload_to='image/')
    about_name = models.CharField(max_length=100)
    about_work = models.CharField(max_length=50)
    about_email = models.EmailField(unique=True, max_length=254)
    about_number = models.IntegerField()
    about_location = models.CharField(max_length=50)
    about_details = models.TextField(blank=True)

    education = models.CharField(max_length=150)
    experience_level = models.CharField(max_length=50)
    years_experience = models.PositiveIntegerField(default=0)

    specialization = models.CharField(
        max_length=200,
        help_text="Comma-separated values e.g. UI/UX, Web Dev"
    )

    languages = models.CharField(
        max_length=200,
        help_text="Comma-separated values e.g. English, Spanish, French"
    )

    def __str__(self):
       return self.about_name



class SkillCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.title


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        related_name="skills",
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(
        help_text="Skill level (0–100)"
    )
    tooltip = models.TextField(
        blank=True,
        help_text="Short description shown on hover"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls display order"
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"


class Education(models.Model):
    title = models.CharField(max_length=200)
    duration = models.CharField(blank=True, max_length=100)
    school = models.CharField(max_length=100)
    descrption = models.TextField()

    def __str__(self):
        return self.title

class Certificate(models.Model):
    certifi = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.certifi

class Experience(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.title
    

class PortfolioCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Portfolio(models.Model):
    portfolio_pics = models.ImageField(upload_to='image/', height_field=None, width_field=None, max_length=None)
    categorys = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.title
    


class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class ServiceBullet(models.Model):
    service = models.ForeignKey(
        Services,
        related_name="bullets",
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255)
    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls bullet display order"
    )

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Service Bullets"

    def __str__(self):
        return f"{self.service.title} - {self.text}"


class Testimonial(models.Model):
    picture = models.ImageField(upload_to='image/', blank=True, null=True)
    name = models.CharField(max_length=100)                                                                 
    subject = models.CharField(max_length=100)
    details = models.TextField(blank=True)


    def __str__(self):
        return f" {self.name}  {self.subject}"
