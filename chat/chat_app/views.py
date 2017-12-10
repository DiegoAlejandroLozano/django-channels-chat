from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):	
	return render(request, 'index.html')

def chat(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse('index'))
	else:
		nombre = request.POST.get('nombre')
		return render(request, 'chat.html', {'nombre':nombre})