from django.shortcuts import render, redirect

from core.models import Evento

# def index(request): 
#     return redirect('/agenda/')

def lista_eventos(request):
    # retorna todos os eventos
    evento = Evento.objects.all()
    # retorna eventos do usuário logado apenas 
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)

    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
