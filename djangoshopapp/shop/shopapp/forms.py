from django import forms
from . import models


class appliancesUploadForm(forms.ModelForm):
    class Meta:
        model = models.appliancesUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class babypUploadForm(forms.ModelForm):
    class Meta:
        model = models.babypUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class booksetcUploadForm(forms.ModelForm):
    class Meta:
        model = models.booksetcUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class computingUploadForm(forms.ModelForm):
    class Meta:
        model = models.computingUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class electronicsUploadForm(forms.ModelForm):
    class Meta:
        model = models.electronicsUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class fashionUploadForm(forms.ModelForm):
    class Meta:
        model = models.fashionUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class gamingUploadForm(forms.ModelForm):
    class Meta:
        model = models.gamingUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class gardenandcoUploadForm(forms.ModelForm):
    class Meta:
        model = models.gardenandcoUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class healthandcoUploadForm(forms.ModelForm):
    class Meta:
        model = models.healthandcoUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class homeandcoUploadForm(forms.ModelForm):
    class Meta:
        model = models.homeandcoUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class industrialandcoUploadForm(forms.ModelForm):
    class Meta:
        model = models.industrialandcoUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class musicalUploadForm(forms.ModelForm):
    class Meta:
        model = models.musicalUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }


class petandcoUploadForm(forms.ModelForm):
    class Meta:
        model = models.petandcoUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }



class phonesandcoUploadForm(forms.ModelForm):
    class Meta:
        model = models.phonesandcoUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }



class sportingUploadForm(forms.ModelForm):
    class Meta:
        model = models.sportingUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }



class supermarketUploadForm(forms.ModelForm):
    class Meta:
        model = models.supermarketUpload
        fields = ['item_name', 'item_description', 'image']
        labels = {
            'item_name': 'Item name',
            'item_description': 'Description',
            'image': 'Item image',
        }

