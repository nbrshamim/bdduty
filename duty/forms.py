from django import forms

class TextForm(forms.Form):
    input_text = forms.CharField(
        label='HSCode',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type any valid HSCode...'})
    )

class AssessVal(forms.Form):
    hscodenbr = forms.CharField(
        label='HSCode',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    assval_text = forms.CharField(
        label='Assessment Value in BDT',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )