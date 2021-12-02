from django import forms

class WordcloudForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput)
    hex_color = forms.CharField(label='hex_color', max_length=7,
        widget=forms.TextInput(attrs={'type': 'color'}))
    
    