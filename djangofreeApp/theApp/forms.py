from django import forms
from . import models


class appUploadForm(forms.ModelForm):
    class Meta:
        model = models.appUpload
        fields = ['title', 'image', 'file']
        labels = {
            'title': 'title',
            'image': 'cover image',
            'file': 'File',
        }

class bookUploadForm(forms.ModelForm):
    class Meta:
        model = models.bookUpload
        fields = ['title', 'image', 'file']
        labels = {
            'title': 'title',
            'image': 'cover Image',
            'file': 'File',
        }


class miscUploadForm(forms.ModelForm):
    class Meta:
        model = models.miscUpload
        fields = ['title', 'image', 'file']
        labels = {
            'title': 'title',
            'image': 'Cover Image',
            'file': 'File',
        }


class moviesUploadForm(forms.ModelForm):
    class Meta:
        model = models.moviesUpload
        fields = ['title', 'image', 'file']
        labels = {
            'title': 'title',
            'image': 'Cover Image',
            'file': 'File',
        }

class appRequestForm(forms.ModelForm):
    class Meta:
        model = models.apprequest
        fields = ['requestname']
        labels = {
            'requestname': 'requestname',
        }

class bookRequestForm(forms.ModelForm):
    class Meta:
        model = models.bookrequest
        fields = ['requestname']
        labels = {
            'requestname': 'requestname',
        }

class miscRequestForm(forms.ModelForm):
    class Meta:
        model = models.miscrequest
        fields = ['requestname']
        labels = {
            'requestname': 'requestname',
        }

class moviesRequestForm(forms.ModelForm):
    class Meta:
        model = models.moviesrequest
        fields = ['requestname']
        labels = {
            'requestname': 'requestname',
        }