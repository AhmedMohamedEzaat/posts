from django import forms 

from .models import Posts


class Postfrom(forms.ModelForm):
    class Meta :
        model = Posts
        # fields = '__all__'
        # fields = ['active','img','content','title']
        exclude =['author']