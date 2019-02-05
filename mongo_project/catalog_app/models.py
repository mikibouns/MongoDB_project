from djongo import models
from django import forms
from django.contrib.auth.models import User


class ReservedDate(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

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
    name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)

    class Meta:
        abstract = True
        ordering = ["name"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
        )

#-----------------------------------------------------------------------------------------------------------------------


class Room(models.Model):
    places = models.DecimalField()
    category = models.EmbeddedModelField(
        model_container=Category
    )
    reserved = models.EmbeddedModelField(
        model_container=ReservedDate
    )
    description = models.TextField()
    price = models.DecimalField()
    img = models.ImageField()

    def __str__(self):
        return str(self._id)

    class Meta:
        abstract = True
        ordering = ["_id"]


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
    name = models.CharField(max_length=64)
    description = models.TextField()
    img = models.ImageField()
    room = models.EmbeddedModelField(
        model_container=Room
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]
