from djongo import models
from django import forms
from django.contrib.auth.models import User


class ReservedDate(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    objects = models.DjongoManager()

    def __str__(self):
        return '{} > {}'.format(self.check_in, self.check_out)

    class Meta:
        abstract = True
        ordering = ["room"]


class ReservedDateForm(forms.ModelForm):
    class Meta:
        model = ReservedDate
        fields = (
            'person',
            'check_in',
            'check_out'
        )

#-----------------------------------------------------------------------------------------------------------------------


class Category(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    objects = models.DjongoManager()

    def __str__(self):
        return str(self.name)

#-----------------------------------------------------------------------------------------------------------------------


class Room(models.Model):
    number = models.DecimalField(unique=True, primary_key=True)
    places = models.DecimalField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reserved = models.EmbeddedModelField(
        model_container=ReservedDate,
        model_form_class=ReservedDateForm
    )
    description = models.TextField()
    price = models.DecimalField()
    img = models.ImageField()
    objects = models.DjongoManager()

    def __str__(self):
        return str(self.number)

    class Meta:
        abstract = True
        ordering = ["number"]


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = (
            'places',
            'category',
            'reserved',
            'description',
            'price',
            'img',
        )

#-----------------------------------------------------------------------------------------------------------------------


class Hotel(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    description = models.TextField()
    img = models.ImageField()
    room = models.EmbeddedModelField(
        model_container=Room,
        model_form_class=RoomForm
    )
    objects = models.DjongoManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]
