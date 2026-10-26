from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Correo Electronico")
    asunto = forms.CharField(label="Asunto", max_length=150)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea)