from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('quando eu subir uma pagina tipo o projeto EbacFood, ele ficaria aqui?')