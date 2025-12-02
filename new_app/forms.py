from django import forms

from new_app.models import ToDo

class DateInput(forms.DateInput):
    input_type = 'date'

class ToDoForm(forms.ModelForm):
    date = forms.DateField(widget= DateInput)
    class Meta:
        model = ToDo
        fields = '__all__'