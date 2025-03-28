from django.shortcuts import render, redirect
from .models import PatchResult
from django.views.decorators.csrf import csrf_exempt

MIDDLEWARES = [
    {"name": "Apache", "slug": "apache"},
    {"name": "Nginx", "slug": "nginx"},
    {"name": "Tomcat", "slug": "tomcat"},
    {"name": "JBoss", "slug": "jboss"},
    {"name": "WebLogic", "slug": "weblogic"},
    {"name": "WAS", "slug": "websphere"},
]

def dashboard(request):
    middlewares = [
        {"name": "Apache", "slug": "apache", "count": 3, "color": "bg-danger", "icon": "fas fa-fire"},
        {"name": "Nginx", "slug": "nginx", "count": 2, "color": "bg-success", "icon": "fas fa-leaf"},
        {"name": "Tomcat", "slug": "tomcat", "count": 1, "color": "bg-warning", "icon": "fas fa-cat"},
        {"name": "JBoss", "slug": "jboss", "count": 4, "color": "bg-primary", "icon": "fas fa-rocket"},
        {"name": "WebLogic", "slug": "weblogic", "count": 2, "color": "bg-purple", "icon": "fas fa-brain"},
        {"name": "WAS", "slug": "websphere", "count": 3, "color": "bg-teal", "icon": "fas fa-cogs"},
    ]
    for mw in middlewares:
        mw["count"] = 0  # temporalmente, luego se conectará a Tower

    return render(request, "dashboard.html", {"middlewares": middlewares})

@csrf_exempt  # Solo para pruebas, en prod gestiona bien el CSRF
def middleware_detail(request, slug):
    if request.method == "POST":
        patch_id = request.POST.get("patch_id")
        patch = PatchResult.objects.get(id=patch_id)
        patch.applied = True
        patch.save()
        return redirect("core:middleware_detail", slug=slug)

    patches = PatchResult.objects.filter(middleware__iexact=slug)
    return render(request, f"middleware/{slug}.html", {"patches": patches, "middleware": slug})
