from django import forms
<<<<<<< HEAD
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta():
        model = Article
        # fields = '__all__'
        exclude = ('user',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
=======
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        exclude = ('article',)
>>>>>>> fdb1a7bf510986878a22a39d23404433d2e59c6d
