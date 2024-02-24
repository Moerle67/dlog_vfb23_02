from django.shortcuts import render
from .models import *

# Create your views here.

#def start(request):

def start(request):
   blog = Blog.objects.all()
   print(blog)
   contents = {
      'branding': 'vfb-weiterbildung.de',
      'user': request.user,
      'blog': blog,
   }
   return render(request, 'blog/start.html', contents) 