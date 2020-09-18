from django import forms
from .models import Projects,Activity,Credit

class ProjectRegisterForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_name', 'temple_name', 'decription', 'tel','email','expected','image']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['username','projectname','amount','user_image','user_title','project_image','project_desc']


class CreditCardForm(forms.ModelForm):
    amount = forms.FloatField()
    class Meta:
        model = Credit
        fields = '__all__'
