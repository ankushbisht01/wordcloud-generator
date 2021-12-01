from django import forms

class WordcloudForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput)
    
    