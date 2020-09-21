from django import forms

class MyFormPage(forms.Form):
    """docstring for ."""
    name=forms.CharField()#creates a textbox
    mail=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    #hidden fields
    botcatcher=forms.CharField(required=False, widget=forms.HiddenInput)

    # catching the bot
    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("Some Automated process found")
        return botcatcher
        
