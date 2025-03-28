from django.db import models

class PatchResult(models.Model):
    middleware = models.CharField(max_length=50)
    host = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    applied = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.middleware} - {self.host}"
