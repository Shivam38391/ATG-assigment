
from django import forms
from .models import CustomUser, BlogPost

class CustomUserForm(forms.ModelForm):
    
    password = forms.CharField(widget= forms.PasswordInput())
    confirm_password = forms.CharField(widget= forms.PasswordInput())
    
    
    class Meta:
        model = CustomUser
        # fields = '__all__'
        exclude = ['is_superadmin', 'is_staff', 'is_admin']       
        
        
        
     # this nonfielderror means at form level not models level   
    def clean(self):
        cleaned_data = super(CustomUserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError("password must be same as confirm_password")
        
        
class BlogPostForm(forms.ModelForm):

    class Meta:

        model = BlogPost

        # fields = ('title', 'author', 'image', 'summary', 'content',)
        # fields = '__all__'
        exclude = ('author',)