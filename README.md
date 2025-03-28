# Middleware Dashboard

Stack profesional para gestión de parches vía Ansible Tower.

```
docker compose exec backend python manage.py makemigrations core
docker compose exec backend python manage.py migrate
```

## Access


1. **Main project**: 

```bash
    export IP4=$(ip -4 -o addr show scope global | awk '{print $4}' | cut -d/ -f1 | grep -v 172)`

    http://${IP4}:8000/
```

    
2. **Django Adminlte**: 

```bash
    docker compose exec -it backend python manage.py createsuperuser
    http://${IP4}:8000/admin
```
