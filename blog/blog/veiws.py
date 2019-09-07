from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import reverse

def redirect_url(request):
	return redirect(reverse('posts_list'))
