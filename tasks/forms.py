from django import forms
from tasks.models import Tasks, StageTasks


class TasksModelForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
