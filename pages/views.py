from django.shortcuts import render
from django.http import HttpResponse #import this for rendering http response without jinja
from django.views import View #parent class for class based views 
from pages.models import Contact_Model
from django.http import HttpResponseRedirect
# Create your views here.

#created home page 
def home(request):
    return HttpResponse("<h1> Welcome to Arsalan's Home Page </h1>")

def contact(request):
    return HttpResponse("<h1> Contact me on my email arsalan.9798@gmail.com </h1>")

#class based views 
#has a method get
class home_oop(View):
    def get(self,request):
        return HttpResponse("<h1> Arsalan's Oop response</h1>")


def member(request,id):
    return HttpResponse("<h1> Team Member ID: {} </h1>".format(id))

def team(request):
    return HttpResponse("<h1> Team Members List </h1>")

def cat_mem(request,cat_id,mem_id):
    return HttpResponse("<h1> the category: {} for member: {} </h1>".format(cat_id,mem_id))

def q_view(request):
    if (request.method=="GET" and 'cat_id' in request.GET and 'mem_id' in request.GET):
        return HttpResponse("<h1> the category: {} for member: {} </h1>".format(request.GET.get('cat_id'),request.GET.get('mem_id')))
        #format(request.GET.get('key')) holds the value of the query string 
    else:
        return HttpResponse("<h1> Team Members List </h1>")

def index_home(request): #using templates
    return render(request,'index.html',{}) #(request,'page_name',{data_in_dynamic_case})

def about_page(request):
    return render (request,'about.html',{'title':'About Page Passed'})
def contact_page(request):
    if (request.method=='GET'): #GET METHOD OF DELETE AND EDIT 
        if (request.GET.get('method')=='delete' and request.GET.get('id')):
            rec=Contact_Model.objects.filter(id=request.GET.get('id')).get()
            rec.delete()
        elif(request.GET.get('method')=='edit' and request.GET.get('id')):
            cnt=Contact_Model.objects.filter(id=request.GET.get('id')).get()
            return render(request,'edit.html',{'title':'Edit Page','row':cnt})

    elif (request.method== 'POST'): #POST METHOD OF EDIT AND FORM SUMBITTION
        if (request.GET.get('method')=='edit' and request.GET.get('id')):
            rec=Contact_Model.objects.filter(id=request.GET.get('id'))
            rec.update(
                name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            return HttpResponseRedirect('/pages/contact_form/')

        # email=request.POST['email']
        # password=request.POST['password']
        # name=request.POST['name']
        # return render (request,'contact.html',{'email':email,'password':password,'name':name})
        else:
            data=Contact_Model(
                name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            data.save()
    cnt=Contact_Model.objects.all()
    return render (request,'contact.html',{'rows':cnt})