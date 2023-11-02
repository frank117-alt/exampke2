from django import forms
from .models import User

class Perfilform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    class Meta:
        model=User
        fields=(
       'username',
       'thumbnail',
       'last_name',
       'email'
       )

    