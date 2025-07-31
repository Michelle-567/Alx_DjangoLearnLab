from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_message(self):
        data = self.cleaned_data['message']
        # Additional custom validation if needed
        return data
