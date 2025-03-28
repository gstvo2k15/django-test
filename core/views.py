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
    stats = []
    for mw in MIDDLEWARES:
        count = PatchResult.objects.filter(middleware__iexact=mw["slug"], applied=False).count()
        stats.append({**mw, "count": count})
    return render(request, "dashboard.html", {"middlewares": stats})

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
