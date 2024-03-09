from django import forms
from datetime import datetime
from .models import FamilyMember

class FamilyMemberForm(forms.ModelForm):
    date_of_birth = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y'), required=False)

    class Meta:
        model = FamilyMember
        fields = '__all__'

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob:
            try:
                # Parse the input date string in dd/mm/yyyy format
                dob = datetime.strptime(dob.strftime('%d/%m/%Y'), '%d/%m/%Y').date()
            except ValueError:
                raise forms.ValidationError("Invalid date format. Please use dd/mm/yyyy.")
        return dob

    def __init__(self, *args, **kwargs):
        super(FamilyMemberForm, self).__init__(*args, **kwargs)



        # self.fields['spouse'].widget = forms.HiddenInput()
        self.fields['spouse'].label_from_instance = lambda obj: f'{obj.id} - {obj.full_name}'
        self.fields['parent'].label_from_instance = lambda obj: f'{obj.id} - {obj.full_name}'


class SelectFemaleForm(forms.Form):
    female_id = forms.IntegerField(
        label='Enter Female Member ID',
        widget=forms.NumberInput(attrs={'type': 'number', 'inputmode': 'numeric', 'pattern': '[0-9]*'}),
        required=True
    )


