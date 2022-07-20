from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Item_shop, Section_shop, Item_base, Type_item_shop
from django.contrib.auth.models import User


class RegistForm(UserCreationForm):
    username = forms.CharField(label="Логин", max_length=70, required=True)
    password1 = forms.CharField(label="Пароль")
    first_name= forms.CharField(required=True, max_length=50, label="Введите группу - отдел/магазин/база")
    password2 = None
    
    
    
    class Meta:
        model = User
        fields = ("username", "password1", "password1", "first_name")


class insertForm(ModelForm):
    class Meta:
        model = Item_shop
        fields = ['название', 'номеротдела', 'тип', 'количество', 'цена']

class updateForm(ModelForm):
    артикул = forms.IntegerField()
    class Meta:
        model = Item_shop
        fields = ['название', 'номеротдела', 'тип', 'количество', 'цена']


class deleteForm(forms.Form):
    артикул = forms.IntegerField(required=True)


class insertSec(ModelForm):
    class Meta:
        model = Section_shop
        fields = ['тип', 'заведующий']

class updateSec(ModelForm):
    номеротдела = forms.IntegerField(required=True)
    class Meta:
        model = Section_shop
        fields = ['тип', 'заведующий']


class deleteSec(forms.Form):
    номеротдела = forms.IntegerField()


class inSecForm(ModelForm):
    артикул = forms.IntegerField(required=True)
    class Meta:
        model = Item_shop
        fields = ['название', 'тип', 'количество', 'цена']

class basainForm(ModelForm):
    class Meta:
        model = Item_base
        fields = ['название', 'тип', 'количество', 'цена']

class basaupForm(ModelForm):
    артикул = forms.IntegerField(required=True)
    class Meta:
        model = Item_base
        fields = ['название', 'тип', 'количество', 'цена']
class basadeleteForm(forms.Form):
    артикул = forms.IntegerField(required=True)
    
class TypeItem(ModelForm):
    class Meta:
        model = Type_item_shop
        fields = ['тип']

class Search(forms.Form):
    название = forms.CharField(label="",max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Название'}))




