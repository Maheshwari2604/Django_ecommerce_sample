from django import forms


class Billform(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Enter your name:"
        }
    ))

    Email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class":"form-control",
            "placeholder":"Enter your Email:"
        }
    ))

    Address = forms.CharField(widget=forms.Textarea(
        attrs={
            "class":"form-control",
            "placeholder":"Your Address"
        }
    ))

    def clean_email(self):
        email = self.cleaned_data.get("Email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be a gmail.com")
        return email
    