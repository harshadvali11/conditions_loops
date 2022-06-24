from django.shortcuts import render

# Create your views here.
def hai(request):
    #d={'name':0}
    d={'a':100,'b':309,'c':60}
    return render(request,'hai.html',context=d)

def looping(request):
    d={'name':'Ashu'}
    return render(request,'looping.html',context=d)