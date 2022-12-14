from django import forms
from .models import Member

from .member_create_data_check import checkSuite

class MemberForm(forms.ModelForm):
    availability = forms.FloatField(required=True, 
                                    label='', 
                                    widget=forms.NumberInput(
        attrs={
            'label': 'availability',
            'placeholder': 'Availability'
            }
        )
    )

    spendable = forms.FloatField(required=True, 
                                 label='', 
                                 widget=forms.NumberInput(
        attrs={
            'label': 'spendable',
            'placeholder': 'Spending limit'
            }
        )
    )

    name = forms.CharField(required=True, 
                               label='', 
                               widget=forms.TextInput(
        attrs={
            'label': 'name',
            'placeholder': 'Name'
            }
        )
    )

    email = forms.CharField(required=True, 
                            label='',
                            widget=forms.EmailInput(
        attrs={
            'label': 'email',
            'placeholder': 'Email'
            }
        )
    )

    author = forms.CharField(label='',
                             disabled=True,
                             widget=forms.TextInput(
        attrs={
            'label': 'Author'
        }
                             ))

    class Meta:
        model = Member
        fields = [
            'availability',
            'spendable',
            'name',
            'email'
        ]

    def clean(self):
        cleaned_data = super(MemberForm, self).clean()

        data_dict = {
            'spendable': cleaned_data.get("spendable"),
            'availability': cleaned_data.get("availability")
        }

        errorList, relations, error_messages_en, error_messages_it = checkSuite(data_dict)
        for error in errorList:
            self.add_error(relations[error], '%s / %s' % (str(error_messages_en[error]), str(error_messages_it[error])))
        
        return cleaned_data