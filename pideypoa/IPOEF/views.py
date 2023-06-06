from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.http import HttpResponse
from .models import indicadores
from .forms import IndicadorForm
from .models import estrategias
from .forms import EstrategiaForm
from .models import areas
from .forms import AreaForm
from .models import programas 
from .forms import ProgramaForm
from .forms import LoginForm

# Create your views here.
def login(request):
    return render (request, 'Auth/login.html')
#def login(request):
#    if request.user.is_authenticated:
#        return redirect('dashboard:dashboard')
#    form = LoginForm(request.POST or None)
#    if form.is_valid():
#        login = form.cleaned_data['login']
#        password = form.cleaned_data['password']
#        usuario = authenticate(request, login=login, password=password)
#        if usuario is not None:
#            auth_login(request, usuario)
#            if 'next' in request.GET:
#                return redirect(request.GET['next'])
#            return redirect("dashboard:dashboard")
#        else:
#            messages.error(request, """Por favor introduzca un nombre de usuario y 
#                        contraseña correctos de su cuenta de SITO. 
#                        Si aún no estás registrado haz clic en el enlace de abajo Regístrate Aquí.""")
#            return redirect('usuario:login')
#    context = {
#        'form': form,
#    }
#    return render(request, 'Auth/login.html', context)

def index(request):
    return render (request, 'paginas/index.html')

#vistas deindicadores
#@login_required(login_url='login')
def indicadoress(request):
    busqueda = request.POST.get("buscar")
    indicadoress = indicadores.objects.all()
    if busqueda: 
        indicadoress = indicadores.objects.filter(
            Q(nombre__icontains = busqueda)|
            Q(valor__icontains = busqueda)|
            Q(año__icontains = busqueda)
        ).distinct()
    
    return render(request, 'indicadores/index.html', {'indicadores': indicadoress})

def crear_indicador(request):
    estrategia = estrategias.objects.all()
    programa = programas.objects.all()
    area = areas.objects.all()
    if request.method == 'POST':
        formulario = IndicadorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('indicadores')
    else:
        formulario = IndicadorForm()
    return render(request,'indicadores/crear.html', {'formulario': formulario, 'estrategia': estrategia, 'programa': programa,'area': area})
   
def editar_indicador(request, id):
    indicadoress = indicadores.objects.get(id=id)
    if request.method == 'POST':
        form = IndicadorForm(request.POST, instance=indicadoress)
        if form.is_valid():
            form.save()
            return redirect('indicadores')
    else:
        form = IndicadorForm(instance=indicadoress)
        estrategiass = estrategias.objects.all()
    return render(request, 'indicadores/editar.html', {'form': form, 'estrategias': estrategiass, 'indicadores': indicadoress})
#def editar_indicador(request, id):
#   indicadoress = indicadores.objects.get(id=id)
#    formulario =IndicadorForm(request.POST or None, request.FILES or None, instance=indicadoress)
#    if formulario.is_valid() and request.method == 'POST':
#        formulario.save()
#        return redirect('indicadores')
#    return render(request, 'indicadores/editar.html', {'formulario':formulario})

def eliminar_indicador(request, id):
    indicadoress = indicadores.objects.get(id=id)
    indicadoress.delete()
    return redirect('indicadores')

#vistas de estrategias
def estrategiass(request):
    estrategiass = estrategias.objects.all()
    return render(request, 'estrategias/index.html', {'estrategias': estrategiass})
def crear_estrategia(request):
    formularioestrategias = EstrategiaForm(request.POST or None, request.FILES or None)
    if formularioestrategias.is_valid():
        formularioestrategias.save()
        return redirect('estrategias')
    return render(request,'estrategias/crear.html', {'formularioestrategias': formularioestrategias})
def editar_estrategia(request, id):
    estrategiass = estrategias.objects.get(id=id)
    formularioestrategias =EstrategiaForm(request.POST or None, request.FILES or None, instance=estrategiass)
    if formularioestrategias.is_valid() and request.method == 'POST':
        formularioestrategias.save()
        return redirect('estrategias')
    return render(request, 'estrategias/editar.html', {'formularioestrategias':formularioestrategias})
def eliminar_estrategia(request, id):
    estrategiass = estrategias.objects.get(id=id)
    estrategiass.delete()
    return redirect('estrategias')

#vistas de areas
def areass(request):
    areass = areas.objects.all()
    return render(request, 'areas/index.html', {'areas': areass})
def crear_area(request):
    formularioareas = AreaForm(request.POST or None, request.FILES or None)
    if formularioareas.is_valid():
        formularioareas.save()
        return redirect('areas')
    return render(request,'areas/crear.html', {'formularioareas': formularioareas})
def editar_area(request, id):
    areass = areas.objects.get(id=id)
    formularioareas =AreaForm(request.POST or None, request.FILES or None, instance=areass)
    if formularioareas.is_valid() and request.method == 'POST':
        formularioareas.save()
        return redirect('areas')
    return render(request, 'areas/editar.html', {'formularioareas':formularioareas})
def eliminar_area(request, id):
    areass = areas.objects.get(id=id)
    areass.delete()
    return redirect('areas')

#vistas de programas
def programass(request):
    programass = programas.objects.all()
    return render(request, 'programas/index.html', {'programas': programass})
def crear_programa(request):
    formularioprogramas = ProgramaForm(request.POST or None, request.FILES or None)
    if formularioprogramas.is_valid():
        formularioprogramas.save()
        return redirect('programas')
    return render(request,'programas/crear.html', {'formularioprogramas': formularioprogramas})
def editar_programa(request, id):
    programass = programas.objects.get(id=id)
    formularioprogramas =ProgramaForm(request.POST or None, request.FILES or None, instance=programass)
    if formularioprogramas.is_valid() and request.method == 'POST':
        formularioprogramas.save()
        return redirect('programas')
    return render(request, 'programas/editar.html', {'formularioprogramas':formularioprogramas})
def eliminar_programa(request, id):
    programass = programas.objects.get(id=id)
    programass.delete()
    return redirect('programas')