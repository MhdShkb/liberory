import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from app.models import Book, Login, district, Area, BookCatogeory, Feedback, Payment, creditcard


class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'type', 'image','price')


class CustomUserform(UserCreationForm):
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    def phone_number_validator(value):
        if not re.compile(r'^[7-9]\d{9}$').match(value):
            raise ValidationError('This is Not a Valid Phone Number')

    phone = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2', 'name', 'phone', 'email', 'address', 'image',)



class Dealerform(UserCreationForm):
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    def phone_number_validator(value):
        if not re.compile(r'^[7-9]\d{9}$').match(value):
            raise ValidationError('This is Not a Valid Phone Number')
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2', 'name', 'phone', 'email', 'address','area',)


class districtform(forms.ModelForm):
    class Meta:
        model = district
        fields = ('name',)


class areaform(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('district_name', 'name',)


class Catogeoryform(forms.ModelForm):
    class Meta:
        model = BookCatogeory
        fields = ('name',)

class DateInput(forms.DateInput):
    input_type = 'date'


class feedbackform(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model = Feedback
        fields = ('title','feedback','date',)

class Paymentform(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('name','bill_date','amount','status',)

class cardform(forms.ModelForm):
    card_no = forms.CharField(validators=[RegexValidator(regex='^.{16}$', message='Please Enter a Valid Card Number')])
    Card_cvv = forms.CharField(widget=forms.PasswordInput,validators=[RegexValidator(regex='^.3$', message='Please Enter a Valid CVV')])
    expiry_date = forms.DateField(widget=DateInput(attrs={'id': 'example-month-input'}))

    class Meta:
        model=creditcard
        fields=('card_no','Card_cvv','expiry_date',)
