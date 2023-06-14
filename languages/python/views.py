from django.shortcuts import render

# Create your views here.
def ds(r):

   dt = {
        'name':'payal',
        'id':101,
        'city':'latur'
    }
   return render (r,'python/ds.html',context=dt)
def Adv(r):
    return render (r,'python/Adv.html')
import datetime
def git(r):
    cdtime =datetime.datetime.now()
    myd ={'cdtime': cdtime}
    return render (r,'python/git.html',context=myd)
