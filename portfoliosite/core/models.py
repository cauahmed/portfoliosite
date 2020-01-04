from django.db import models

# About model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"

# Skill Model
class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Skill title")
    description = models.TextField(verbose_name="Skill description")

    def __str__(self):
        return self.name

# Completed Projects Model
class CompletedProject(models.Model):
    project_id = models.CharField(max_length=2, verbose_name="Project Id")
    title = models.CharField(max_length=100, verbose_name="Project title")
    image = models.ImageField(upload_to="projects")
    description = models.TextField(verbose_name="Project description")
    project_link = models.TextField(verbose_name="Project Link")

    def __str__(self):
        return self.title

#Client Model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client description")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name

#Contact Model
class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fullname
        
#Cetifications Model
class Certification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Certificate description")
    image = models.ImageField(upload_to="certs", default="default.png")
    attachment_address = models.TextField(verbose_name="Attachment Address")

    def __str__(self):
        return self.title
