from django import forms
from .models import indicadores
from .models import estrategias
from .models import areas
from .models import programas
from .models import login

class IndicadorForm(forms.ModelForm):
    class Meta:
        model = indicadores
        fields ='__all__'
    

class EstrategiaForm(forms.ModelForm):
    class Meta:
        model = estrategias
        fields ='__all__'

class AreaForm(forms.ModelForm):
    class Meta:
        model = areas
        fields ='__all__'

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = programas
        fields ='__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields ='__all__'