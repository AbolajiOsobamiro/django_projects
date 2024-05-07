from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories.html', views.categories, name='categories'),
    path('supermarket.html', views.supermarket, name='supermarket'),
    path('supermarketupload.html', views.supermarketupload, name='supermarketupload'),
    path('supersearch.html', views.supersearch, name='supersearch'),
    path('healthandbeauty.html', views.health, name='healthandbeauty'),
    path('healthandbeautyupload.html', views.healthupload, name='healthandbeautyupload'),
    path('healthsearch.html', views.healthsearch, name='healthsearch'),
    path('appliances.html', views.appliances, name='appliances'),
    path('appliancesupload.html', views.appliancesupload, name='appliancesupload'),
    path('appsearch.html', views.appsearch, name='appsearch'),
    path('babyproducts.html', views.babyp, name='babyproducts'),
    path('babyproductsupload.html', views.babypupload, name='babypupload'),
    path('babsearch.html', views.babsearch, name='babsearch'),
    path('booksmoviesandmusic.html', views.books, name='books'),
    path('booksmoviesandmusicupload.html', views.booksetcupload, name='booksetcupload'),
    path('booksearch.html', views.booksearch, name='booksearch'),
    path('computing.html', views.computing, name='computing'),
    path('computingupload.html', views.computingupload, name='computingupload'),
    path('compsearch.html', views.compsearch, name='compsearch'),
    path('electronics.html', views.electronics, name='electronics'),
    path('electronicsupload.html', views.electronicsupload, name='electronicsupload'),
    path('elecsearch.html', views.elecsearch, name='elecsearch'),
    path('fashion.html', views.fashion, name='fashion'),
    path('fashionupload.html', views.fashionupload, name='fashionupload'),
    path('fashsearch.html', views.fashsearch, name='fashsearch'),
    path('gaming.html', views.gaming, name='gaming'),
    path('gaminguploads.html', views.gamingupload, name='gamingupload'),
    path('gamsearch.html', views.gamsearch, name='gamsearch'),
    path('gardenandoutdoors.html', views.garden, name='garden'),
    path('gardenandoutdoorsuploads.html', views.gardenupload, name='gardenupload'),
    path('gardensearch.html', views.gardensearch, name='gardensearch'),
    path('homeandoffice.html', views.home, name='home'),
    path('homeandofficeupload.html', views.homeupload, name='homeupload'),
    path('homesearch.html', views.homesearch, name='homesearch'),
    path('industrialandscientific.html', views.industrial, name='industrial'),
    path('industrialandscientificupload.html', views.industrialupload, name='industrialupload'),
    path('indusearch.html', views.indusearch, name='indusearch'),
    path('musicalinstruments.html', views.musical, name='musical'),
    path('musicalinstrumentsupload.html', views.musicalupload, name='musicalupload'),
    path('musicsearch.html', views.musicsearch, name='musicsearch'),
    path('mycart.html', views.mycart, name='mycart'),
    path('phonesandtablets.html', views.phones, name='phones'),
    path('phonesandtabletsupload.html', views.phonesupload, name='phonesupload'),
    path('phonesearch.html', views.phonesearch, name='phonesearch'),
    path('petsupplies.html', views.pets, name='pets'),
    path('petsuppliesupload.html', views.petsupload, name='petsupload'),
    path('petsearch.html', views.petsearch, name='petsearch'),
    path('sellerspage.html', views.sellers, name='sellers'),
    path('sportinggoods.html', views.sporting, name='sporting'),
    path('sportinggoodsupload.html', views.sportingupload, name='sportingupload'),
    path('sportsearch.html', views.sportsearch, name='sportsearch'),
    path('signup.html', views.signup, name='signup'),
    path('logout', views.logout, name= 'logout'),
    path('login.html', views.login, name='login'),

]