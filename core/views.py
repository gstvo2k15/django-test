from django.shortcuts import render
from .models import PatchResult

def dashboard(request):
    middlewares = [
        {"name": "Apache", "slug": "apache", "count": 3},
        {"name": "Nginx", "slug": "nginx", "count": 2},
        {"name": "Tomcat", "slug": "tomcat", "count": 4},
        {"name": "Jboss", "slug": "jboss", "count": 7},        
        {"name": "Weblogic", "slug": "weblogic", "count": 6},
        {"name": "WAS", "slug": "was", "count": 1},
    ]
    return render(request, "dashboard.html", {"middlewares": middlewares})

def middleware_detail(request, slug):
    patches = PatchResult.objects.filter(middleware__iexact=slug)
    return render(request, f"middleware/{slug}.html", {"patches": patches, "middleware": slug})
