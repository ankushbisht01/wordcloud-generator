from django.shortcuts import render
from main import forms
from django.http import HttpResponse
from wordcloudImages import ImageGen
# Create your views here.


def index(request):
    form = forms.WordcloudForm()
    colormaps = ['Paste1', 'Paste2', 'Paired', 'Accent', 'Dark2',
                 'set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c']
    context = {
        'form': form,
        'colormap': colormaps
    }
    if request.method == 'POST':
        form = forms.WordcloudForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            colormap = request.POST['options']
            bgcolor =  form.cleaned_data['hex_color']
            
            Image = ImageGen()
            content = Image.normal_wordcloud(text,colormap,bgcolor)
            url = Image.upload(content)
            colormaps = ['autumn','binary', 'gist_yarg', 'gist_gray', 'gray', 'bone','pink', 'spring', 'summer',  'winter', 'cool','Wistia', 'hot', 'afmhot', 'gist_heat', 'copper','twilight', 'twilight_shifted', 'hsv','PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu','RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic','Paste1', 'Paste2', 'Paired', 'Accent', 'Dark2',
                         'set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c']
            context = {
                'flag': True,
                'url': url,
                'colormap': colormaps,
            }
            return render(request, 'main/index.html', context=context)

    return render(request, 'main/index.html', context)

# Create your views here.
