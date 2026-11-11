from django import forms
from .models import Project

class ProjectForm(form.ModelForm):
    class Meta:
        model = Project
        feilds = '__all__'