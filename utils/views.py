from django.http import HttpResponse


def index(request):
	return HttpResponse('Hello from utils: {}'.format(request.get_raw_uri()))
