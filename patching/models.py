from django.db import models

class Server(models.Model):
    hostname = models.CharField(max_length=128)
    ip_address = models.GenericIPAddressField()
    os = models.CharField(max_length=64)
    group = models.CharField(max_length=64)

class Middleware(models.Model):
    MIDDLEWARE_CHOICES = [
        ('apache', 'Apache'),
        ('nginx', 'Nginx'),
        ('jboss', 'JBoss'),
        ('tomcat', 'Tomcat'),
        ('weblogic', 'WebLogic'),
        ('was', 'WebSphere'),
    ]
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    type = models.CharField(max_length=32, choices=MIDDLEWARE_CHOICES)
    installed_version = models.CharField(max_length=32)
    latest_version = models.CharField(max_length=32)
    patched = models.BooleanField(default=False)

class PatchingStatus(models.Model):
    middleware = models.ForeignKey(Middleware, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Completed'),
        ('failed', 'Failed'),
    ])
    last_run = models.DateTimeField(auto_now=True)
    log = models.TextField(blank=True, null=True)
