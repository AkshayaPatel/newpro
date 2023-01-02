from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def form_view(request):
    form= forms.Form()
    if request.method== 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            print("Validation success")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])
    return  render(request,'basicapp/form.html',{'form':form})

# create a function
