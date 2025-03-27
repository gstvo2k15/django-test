import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

TOWER_API_URL = os.getenv("TOWER_API_URL")
TOWER_API_TOKEN = os.getenv("TOWER_API_TOKEN")

class LaunchPatchJobView(APIView):
    def post(self, request):
        middleware = request.data.get("middleware")
        host = request.data.get("host")

        if not middleware or not host:
            return Response({"error": "middleware and host required"}, status=status.HTTP_400_BAD_REQUEST)

        # Mapea cada middleware con su job_template_id en Tower
        job_templates = {
            "Apache": 21,
            "Nginx": 22,
            "Tomcat": 23,
            "JBoss": 24,
            "WebLogic": 25,
            "WAS": 26
        }

        template_id = job_templates.get(middleware)
        if not template_id:
            return Response({"error": "Invalid middleware"}, status=status.HTTP_400_BAD_REQUEST)

        headers = {
            "Authorization": f"Bearer {TOWER_API_TOKEN}",
            "Content-Type": "application/json"
        }

        launch_url = f"{TOWER_API_URL}job_templates/{template_id}/launch/"
        payload = {
            "extra_vars": {
                "target_host": host
            }
        }

        response = requests.post(launch_url, json=payload, headers=headers)

        if response.status_code in [201, 202]:
            return Response({"message": "Patch job launched", "job_id": response.json().get("job")})
        else:
            return Response({"error": "Tower error", "detail": response.text}, status=response.status_code)
