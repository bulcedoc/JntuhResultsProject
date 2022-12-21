from django import forms

class Sign(forms.Form):
    roll = forms.CharField( max_length=10, required=True)
    s_n = forms.CharField( max_length=10, required=True)
    pic = forms.ImageField(required=False)

class Login(forms.Form):
    roll = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class':'d','required':'True'}))
    