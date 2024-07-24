from django import forms

class CursoFormulario (forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class BuscarCursoForm (forms.Form):
    curso = forms.CharField(max_length=10)
    camada = forms.IntegerField(required=False)