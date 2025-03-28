from django.shortcuts import render, redirect
from .models import PatchResult
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.db.models.functions import TruncDay
import json

MIDDLEWARES = [
    {"name": "Apache", "slug": "apache", "color": "bg-danger", "icon": "fas fa-fire"},
    {"name": "Nginx", "slug": "nginx", "color": "bg-success", "icon": "fas fa-leaf"},
    {"name": "Tomcat", "slug": "tomcat", "color": "bg-warning", "icon": "fas fa-cat"},
    {"name": "JBoss", "slug": "jboss", "color": "bg-primary", "icon": "fas fa-rocket"},
    {"name": "WebLogic", "slug": "weblogic", "color": "bg-purple", "icon": "fas fa-brain"},
    {"name": "WAS", "slug": "websphere", "color": "bg-teal", "icon": "fas fa-cogs"},
]

def dashboard(request):
    middlewares = []
    bar_data = []

    for mw in MIDDLEWARES:
        count = PatchResult.objects.filter(middleware__iexact=mw["slug"], applied=False).count()
        mw_data = mw.copy()
        mw_data["count"] = count
        middlewares.append(mw_data)
        bar_data.append(count)

    # Línea de tiempo de parches pendientes por día
    timeline_data = (
        PatchResult.objects
        .filter(applied=False)
        .annotate(day=TruncDay("timestamp"))
        .values("day")
        .annotate(count=Count("id"))
        .order_by("day")
    )

    labels = [entry["day"].strftime("%d %b") for entry in timeline_data]
    line_data = [entry["count"] for entry in timeline_data]

    context = {
        "middlewares": middlewares,
        "chart_labels": json.dumps(labels),
        "chart_data": json.dumps(line_data),
        "bar_data": json.dumps(bar_data),
    }

    return render(request, "dashboard.html", context)

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
