from django.db import models
from django.contrib.auth.models import User

class IntegerRangeField(models.IntegerField):
    def __init__(self,verbose_name=None,name=None,min_value=None,max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class DecimalRangeField(models.DecimalField):
    def __init__(self,verbose_name=None,name=None,min_value=None,max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.DecimalField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(DecimalRangeField, self).formfield(**defaults)

class WebUser(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    user = models.OneToOneField(User)
    email = models.EmailField()
    age = IntegerRangeField(min_value=18)
    def __unicode__(self):
        return self.name + self.surname

class Shop(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    email = models.EmailField()
    def __unicode__(self):
        return self.name+"("+self.url+")"

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name+"("+self.category+")"

class Price(models.Model):
    shop = models.ForeignKey(Shop)
    item = models.ForeignKey(Item)
    price = DecimalRangeField(min_value=0.0,decimal_places=2,max_digits=9)
    
class RatingShop(models.Model):
    webUser = models.ForeignKey(WebUser)
    shop = models.ForeignKey(Shop)
    value = IntegerRangeField(min_value=1,max_value=5)
    
class RatingItem(models.Model):
    webUser = models.ForeignKey(WebUser)
    item = models.ForeignKey(Item)
    value = IntegerRangeField(min_value=1,max_value=5)
    