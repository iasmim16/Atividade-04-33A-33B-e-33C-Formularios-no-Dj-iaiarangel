from django.shortcuts import render, redirect
from .models import Beneficios, Principios

# Create your views here.
def home(request):
  beneficios = Beneficios.objects.all()
  principios = Principios.objects.all()
  
  return render(request, "home.html", context={
    "beneficios": beneficios,
    "principios": principios
  })
  
def create_beneficios(request):
  if request.method == "POST":
    Beneficios.objects.create(
      categoria = request.POST["categoria"],
      intensidade = request.POST["intensidade"],
      melhoria = request.POST["melhoria"],
      como_fazer = request.POST["como_fazer"]
    )
    return redirect("home")
  return render(request, "forms.html", context={"type": "Adicionar"})

def update_beneficios(request, id):
  beneficios = Beneficios.objects.get(id = id)
  if request.method == "POST":
    beneficios.categoria = request.POST["categoria"]
    beneficios.intensidade = request.POST["intensidade"]
    beneficios.melhoria = request.POST["melhoria"]
    beneficios.como_fazer = request.POST["como_fazer"]
    beneficios.sav()
    
    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar" , "beneficios" : beneficios})

def delete_beneficios(request, id):
  beneficios = Beneficios.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      beneficios.delete()
    
    
    return redirect("home")
  return render(request, "are_you_sure.html", context={"beneficios": beneficios})

