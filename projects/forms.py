from django.forms import ModelForm
from .models import ProjectsModel
from django import forms
class ProjectsForm(ModelForm):
    class Meta:
        model = ProjectsModel
        fields = ['title', 'description', 'featured_image',  'vote_ratio', 'vote_total', 'tags', 'source_link', 'demo_link']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    #
    # def __init__(self, *args, **kwargs):
    #     super(ProjectsForm, self).__init__(self, *args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'input'})

    def __init__(self, *args, **kwargs):
        super(ProjectsForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add title'})