from django.shortcuts import render
from .forms import RegistrationModel
from django.http import HttpResponseRedirect

# Create your views here.
def test(r):
    form = RegistrationModel()
    if r.method == 'POST':
        form = RegistrationModel(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/feedback')

    return render(r, 'feedback.html', {'form':form})


