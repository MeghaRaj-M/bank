from django import forms
from .models import District, Branch


class AccountForm(forms.Form):
    name = forms.CharField()
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[("male", "Male"), ("female", "Female"), ("others", "Others")])
    phone = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label=None, required=True,
                                      widget=forms.Select(attrs={'id': 'district'}))
    branch = forms.ModelChoiceField(queryset=Branch.objects.none(), required=False,
                                    widget=forms.Select(attrs={'id': 'branch'}))
    account_type = forms.ChoiceField(
        choices=[("savings", "Savings Account"), ("current", "Current Account"), ("salary", "Salary Account")])
    materials_provide = forms.MultipleChoiceField(
        choices=[("debit", "Debit Card"), ("credit", "Credit Card"), ("cheque", "Cheque Book")],
        widget=forms.CheckboxSelectMultiple()
    )
