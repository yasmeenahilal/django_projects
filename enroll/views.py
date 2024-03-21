from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
#This Function Will Add New Items AND Show All Items
def add_show(request):
    stud = User.objects.all()  # Move this line outside of the else block

    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            form.save()
    else:
        form = StudentRegistration()

    return render(request, 'enroll/addandshow.html', {'form': form, 'stu': stud})

#This Function will update/Edit
def update_data(request,id):
        pi = User.objects.get(pk=id)

        if request.method == 'POST':
            fm = StudentRegistration(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
        else:
            pi = User.objects.get(pk=id)
            fm = StudentRegistration( instance=pi)

        return render(request, 'enroll/updatestudent.html',{'form':fm,'id':id})


#This Function Will Delete
def delete_data(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
