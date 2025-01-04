from django.db import models

from spark_api_drf_main.contact_app.api.serializers import User

ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('visitor', 'Visitor'),
    ('editor', 'Editor'),
    ('contributor', 'Contributor'),
]
# Create your models here.
class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='admin'
    )
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
 
class RoleEcommerce(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='visitor',
    )
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
class RoleAcademia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='visitor',
    )
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
class RoleEvents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='visitor',
    )
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
class RoleEquipes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='visitor',
    )
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

class RolePublicites(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='visitor',
    )
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
  
#admin     read write update delete (create subscriptions) can approve and decide who is editor
#visitor    read
#contributor    read write update delete with approval
#editor    read write delete can approval

