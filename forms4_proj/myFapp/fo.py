from django import forms

class UserForm(forms.Form):
    name=forms.CharField()
    mail=forms.EmailField()
    varify_mail=forms.EmailField(label='Please verify your Mail ID')
    text=forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data=super().clean()
        fmail=all_clean_data['mail']
        vmail=all_clean_data['varify_mail']

        if fmail != vmail:
            raise forms.ValidationError('Email not match!')
