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
            "description": "Description",
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("startTime")
        end_time = cleaned_data.get("endTime")

        if start_time and end_time and end_time <= start_time:
            raise forms.ValidationError("End time must be after the start time.")

        return cleaned_data


class ImportICSForm(forms.Form):
    ics_file = forms.FileField(
        label="Select an .ics file", help_text="File should be in .ics format"
    )
