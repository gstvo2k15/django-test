# Middleware Dashboard

Stack profesional para gestión de parches vía Ansible Tower.

```
docker compose exec backend python manage.py makemigrations core
docker compose exec backend python manage.py migrate
```

## Access

`export IP4=$(ip -4 -o addr show scope global | awk '{print $4}' | cut -d/ -f1 | grep -v 172)`

1. **Main project: `http://${IP4}:8000/`

2. **Django Adminlte: `http://${IP4}:8000/admin`
