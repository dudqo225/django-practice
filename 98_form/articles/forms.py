from django import forms
from django.forms import fields
from .models import Article

class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #         }
    #     )
    # )

    class Meta():
        model = Article
        fields = '__all__'

