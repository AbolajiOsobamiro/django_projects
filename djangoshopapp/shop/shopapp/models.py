from django.db import models


class appliancesUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class booksetcUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name

class babypUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')
    
    def __str__(self):
        return self.item_name


class computingUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')


class electronicsUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class fashionUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class gamingUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class gardenandcoUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class healthandcoUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class homeandcoUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class industrialandcoUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class musicalUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class petandcoUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class phonesandcoUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name



class sportingUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name


class supermarketUpload(models.Model):
    item_name=models.CharField(max_length=1000)
    item_description=models.CharField(max_length=100000000000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')

    def __str__(self):
        return self.item_name