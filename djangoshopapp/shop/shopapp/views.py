from django.shortcuts import render,redirect
from django.conf import settings
from django.http import Http404, HttpResponse
import os
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from . import forms 
from . import models


def index(request):
        instance1 = models.appliancesUpload.objects.all()
        instance2 = models.computingUpload.objects.all()
        instance3 = models.fashionUpload.objects.all()
        instance4 = models.gamingUpload.objects.all()
        instance5 = models.electronicsUpload.objects.all()
        instance6 = models.supermarketUpload.objects.all()
        return render(request, 'index.html', {'instance1':instance1, 'instance2':instance2,
                                              'instance3':instance3, 'instance4':instance4,
                                              'instance5':instance5, 'instance6':instance6})

def supermarket(request):
        instance = models.supermarketUpload.objects.all()
        return render(request, 'supermarket.html', {'instance':instance})

def categories(request):
        return render(request, 'categories.html')

def supermarket(request):
        instance = models.supermarketUpload.objects.all()
        return render(request, 'supermarket.html', {'instance':instance})

def health(request):
        instance = models.healthandcoUpload.objects.all()
        return render(request, 'healthandbeauty.html', {'instance':instance})

def appliances(request):
        instance = models.appliancesUpload.objects.all()
        return render(request, 'appliances.html', {'instance':instance})


def babyp(request):
        instance = models.babypUpload.objects.all()
        return render(request, 'babyproducts.html', {'instance':instance})


def books(request):
        instance = models.booksetcUpload.objects.all()
        return render(request, 'booksmoviesandmusic.html', {'instance':instance})

def computing(request):
        instance = models.computingUpload.objects.all()
        return render(request, 'computing.html', {'instance':instance})

def electronics(request):
        instance = models.electronicsUpload.objects.all()
        return render(request, 'electronics.html', {'instance':instance})


def fashion(request):
        instance = models.fashionUpload.objects.all()
        return render(request, 'fashion.html', {'instance':instance})

def gaming(request):
        instance = models.gamingUpload.objects.all()
        return render(request, 'gaming.html', {'instance':instance})

def garden(request):
        instance = models.gardenandcoUpload.objects.all()
        return render(request, 'gardenandoutdoors.html', {'instance':instance})


def home(request):
        instance = models.homeandcoUpload.objects.all()
        return render(request, 'homeandoffice.html', {'instance':instance})

def industrial(request):
        instance = models.industrialandcoUpload.objects.all()
        return render(request, 'industrialandscientific.html', {'instance':instance})

def musical(request):
        instance = models.musicalUpload.objects.all()
        return render(request, 'musicalinstruments.html', {'instance':instance})

def mycart(request):
        instance = models.musicalUpload.objects.all()
        return render(request, 'mycart.html', {'instance':instance})

def phones(request):
        instance = models.phonesandcoUpload.objects.all()
        return render(request, 'phonesandtablets.html', {'instance':instance})


def pets(request):
        instance = models.petandcoUpload.objects.all()
        return render(request, 'petsupplies.html', {'instance':instance})

def sellers(request):
        instance = models.booksetcUpload.objects.all()
        return render(request, 'sellerspage.html', {'instance':instance})

def sporting(request):
        instance = models.sportingUpload.objects.all()
        return render(request, 'sportinggoods.html', {'instance':instance})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
            
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')


def appliancesupload(request):
        form = forms.appliancesUploadForm()
        if request.method == 'POST':

                form = forms.appliancesUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.appliancesUploadForm()
                        return render(request, "appliancesupload.html", {"form": form})
                        
        else:
                return render(request, 'appliancesupload.html', {"form": form})
        

def babypupload(request):
        form = forms.babypUploadForm()
        if request.method == 'POST':

                form = forms.babypUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.babypUploadForm()
                        return render(request, "babyproductsupload.html", {"form": form})
                        
        else:
                return render(request, 'babyproductsupload.html', {"form": form})
        

def computingupload(request):
        form = forms.computingUploadForm()
        if request.method == 'POST':

                form = forms.computingUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.computingUploadForm()
                        return render(request, "computingupload.html", {"form": form})
                        
        else:
                return render(request, 'computingupload.html', {"form": form})
        

def booksetcupload(request):
        form = forms.booksetcUploadForm()
        if request.method == 'POST':

                form = forms.booksetcUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.booksetcUploadForm()
                        return render(request, "booksmoviesandmusicupload.html", {"form": form})
                        
        else:
                return render(request, 'booksmoviesandmusicupload.html', {"form": form})
        

def electronicsupload(request):
        form = forms.electronicsUploadForm()
        if request.method == 'POST':

                form = forms.electronicsUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.electronicsUploadForm()
                        return render(request, "electronicsupload.html", {"form": form})
                        
        else:
                return render(request, 'electronicsupload.html', {"form": form})
        


def fashionupload(request):
        form = forms.fashionUploadForm()
        if request.method == 'POST':

                form = forms.fashionUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.fashionUploadForm()
                        return render(request, "fashionupload.html", {"form": form})
                        
        else:
                return render(request, 'fashionupload.html', {"form": form})
        


def gamingupload(request):
        form = forms.gamingUploadForm()
        if request.method == 'POST':

                form = forms.gamingUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.gamingUploadForm()
                        return render(request, "gaminguploads.html", {"form": form})
                        
        else:
                return render(request, 'gaminguploads.html', {"form": form})


def phonesupload(request):
        form = forms.phonesandcoUploadForm()
        if request.method == 'POST':

                form = forms.phonesandcoUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.phonesandcoUploadForm()
                        return render(request, "phonesandtabletsupload.html", {"form": form})
                        
        else:
                return render(request, 'phonesandtabletsupload.html', {"form": form})
        

def sportingupload(request):
        form = forms.sportingUploadForm()
        if request.method == 'POST':

                form = forms.sportingUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.sportingUploadForm()
                        return render(request, "sportinggoodsupload.html", {"form": form})
                        
        else:
                return render(request, 'sportinggoodsupload.html', {"form": form})
        

def petsupload(request):
        form = forms.petandcoUploadForm()
        if request.method == 'POST':

                form = forms.petandcoUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.petandcoUploadForm()
                        return render(request, "petsuppliesupload.html", {"form": form})
                        
        else:
                return render(request, 'petsuppliesupload.html', {"form": form})
        


def musicalupload(request):
        form = forms.musicalUploadForm()
        if request.method == 'POST':

                form = forms.musicalUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.musicalUploadForm()
                        return render(request, "musicalinstrumentsupload.html", {"form": form})
                        
        else:
                return render(request, 'musicalinstrumentsupload.html', {"form": form})
        


def healthupload(request):
        form = forms.healthandcoUploadForm()
        if request.method == 'POST':

                form = forms.healthandcoUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.healthandcoUploadForm()
                        return render(request, "healthandbeautyyupload.html", {"form": form})
                        
        else:
                return render(request, 'healthandbeautyupload.html', {"form": form})
        

def supermarketupload(request):
        form = forms.supermarketUploadForm()
        if request.method == 'POST':

                form = forms.supermarketUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.supermarketUploadForm()
                        return render(request, "supermarketupload.html", {"form": form})
                        
        else:
                return render(request, 'supermarketupload.html', {"form": form})
        


def gardenupload(request):
        form = forms.gardenandcoUploadForm()
        if request.method == 'POST':

                form = forms.gardenandcoUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.gardenandcoUploadForm()
                        return render(request, "gardenandoutdoorsuploads.html", {"form": form})
                        
        else:
                return render(request, 'gardenandoutdoorsuploads.html', {"form": form})
        


def homeupload(request):
        form = forms.homeandcoUploadForm()
        if request.method == 'POST':

                form = forms.homeandcoUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.homeandcoUploadForm()
                        return render(request, "homeandofficeupload.html", {"form": form})
                        
        else:
                return render(request, 'homeandofficeupload.html', {"form": form})
        


def industrialupload(request):
        form = forms.industrialandcoUploadForm()
        if request.method == 'POST':

                form = forms.industrialandcoUploadForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save();
                        return redirect("sellerspage.html")
                else:
                        form = forms.industrialandcoUploadForm()
                        return render(request, "industrialandscientificupload.html", {"form": form})
                        
        else:
                return render(request, 'industrialandscientificupload.html', {"form": form})


def appsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.appliancesUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'appsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'appsearch.html')
       

def babsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.babypUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'babsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'babsearch.html')
       

def booksearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.booksetcUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'booksearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'booksearch.html')
       

def compsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.computingUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'compsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'compsearch.html')
       


def elecsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.electronicsUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'elecsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'elecsearch.html')
       

def fashsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.fashionUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'fashsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'fashsearch.html')
       

def gamsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.gamingUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'gamsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'gamsearch.html')
       

def gardensearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.gardenandcoUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'gardensearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'gardensearch.html')
       


def healthsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.healthandcoUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'healthsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'healthsearch.html')
       

def homesearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.homeandcoUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'homesearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'homesearch.html')
       

def indusearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.industrialandcoUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'indusearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'indusearch.html')
       


def musicsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.musicalUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'musicsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'musicsearch.html')
       

def petsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.petandcoUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'petsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'petsearch.html')
       

def phonesearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.phonesandcoUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'phonesearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'phonesearch.html')
       

def sportsearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.sportingUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'sportsearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'sportsearch.html')
       

def supersearch(request):
       if request.method == 'POST':
              searched = request.POST['searched']
              instances = models.supermarketUpload.objects.filter(item_name__contains=searched)
              number = len(instances)
              return render(request, 'supersearch.html', {'searched': searched, 'instances':instances, 'number':number})
       else:
              return render(request, 'supersearch.html')