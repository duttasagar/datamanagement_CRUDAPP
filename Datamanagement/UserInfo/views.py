from django.shortcuts import render
from .forms import Userform
from .models import Usermodel
from django.http import HttpResponseRedirect


# ================================Add and Show functionality=========================================
def form(request):
    if request.method == "POST":
        form = Userform(request.POST)
        form.save()
        return HttpResponseRedirect("/")
    else:
        form = Userform()
        userdata = Usermodel.objects.all()
    return render(request , "form.html" , {'form' : form , 'userdata': userdata})


#===================================Delete Functionality============================================
def deletedata(request , id):
    if request.method == "POST":
        delete_data= Usermodel.objects.get(pk=id)
        delete_data.delete()
        return HttpResponseRedirect("/")
    

#===================================Update functionality==============================================
def updatedata(request , id):
    if request.method == "POST":
        data = Usermodel.objects.get(pk = id)
        edit = Userform(request.POST , instance=data)
        if edit.is_valid():
         edit.save()
         return HttpResponseRedirect("/")
         
    else:
        data = Usermodel.objects.get(pk = id)
        edit = Userform( instance=data)
    return render(request , "update1.html", {'form': edit })



#====================================Search Functionality==========================================
def search(request):
        querydata = request.GET.get('q')
        dt = Usermodel.objects.filter(name = querydata )
        return render(request , "search.html" , {'searchdata': dt })
    