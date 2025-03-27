from django.shortcuts import render
from .models import PatchingStatus

def dashboard(request):
    patches = PatchingStatus.objects.select_related('middleware', 'middleware__server')
    return render(request, 'patching/dashboard.html', {'patches': patches})
