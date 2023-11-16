from django import forms


class PostForm(forms.Form):
    name = forms.CharField(required=False)