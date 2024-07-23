from django import forms 
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'dob':forms.TextInput(attrs={'type':'date','class':'form-control'}),
            'skills' :  forms.CheckboxSelectMultiple(),
            'profession':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'mob_no':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'about':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.ImageField(),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
        }
