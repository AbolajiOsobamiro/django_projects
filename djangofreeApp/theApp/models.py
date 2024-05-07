from django.db import models



class appUpload(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')
    file= models.FileField(upload_to='actualFiles/Apps/')


    def __str__(self):
        return self.title

class bookUpload(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Books/')
    file=models.FileField(upload_to='actualFiles/Books/')


    def __str__(self):
        return self.title

class miscUpload(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Others/')
    file=models.FileField(upload_to='actualFiles/Others/')

    def __str__(self):
        return self.title



class moviesUpload(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Videos/')
    file=models.FileField(upload_to='actualFiles/Videos/')

    def __str__(self):
        return self.title


class apprequest(models.Model):
    requestname =models.CharField(max_length=10000000000000000)

    def __str__(self):
        return self.requestname

class bookrequest(models.Model):
    requestname =models.CharField(max_length=10000000000000000)

    def __str__(self):
        return self.requestname
    
class miscrequest(models.Model):
    requestname =models.CharField(max_length=10000000000000000)

    def __str__(self):
        return self.requestname

class moviesrequest(models.Model):
    requestname =models.CharField(max_length=10000000000000000)

    def __str__(self):
        return self.requestname