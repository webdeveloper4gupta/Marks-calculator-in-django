from django.shortcuts import render
from .forms import mahajan

def aman(request):

    fm=mahajan()
    total=0
    percentage=0
    if request.method=="POST":
        n1=int(request.POST.get("n1"))
        n2=int(request.POST.get("n2"))
        n3=int(request.POST.get("n3"))
        n4=int(request.POST.get("n4"))
        n5=int(request.POST.get("n5"))
        total=n1+n2+n3+n4+n5
        percentage=(total*100)/500




    return render(request,"index.html",{'form':fm,"percentage":percentage,"total":total})   
   

