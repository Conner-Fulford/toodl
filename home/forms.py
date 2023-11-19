from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "startTime", "endTime"]
        widgets = {
            "title": forms.TextInput(attrs={"required": "required"}),
            "description": forms.Textarea(
                attrs={"rows": 4, "style": "resize: vertical;"}
            ),
            "startTime": forms.DateTimeInput(
                attrs={"type": "datetime-local", "required": "required"}
            ),
            "endTime": forms.DateTimeInput(
                attrs={"type": "datetime-local", "required": "required"}
            ),
        }
        labels = {
            "description": "Description",  # Set the label for the description field
        }


class ImportICSForm(forms.Form):
    ics_file = forms.FileField(
        label="Select an .ics file", help_text="File should be in .ics format"
    )
