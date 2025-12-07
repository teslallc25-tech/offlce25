from django.db import models

# Create your models here.
from django.db import models

class TestUser(models.Model):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255)  # plain text (testing only)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username or self.email or self.phone_number}"
