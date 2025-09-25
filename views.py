import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def api(request):
	time.sleep(1)
	payload = {"message": "Hello from Crowdbotics!"}
	if "task_id" in request.GET:
		payload["task_id"] = request.GET["task_id"]
	return JsonResponse(payload)