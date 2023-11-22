from datetime import datetime, timedelta
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from home.forms import EventForm, ImportICSForm


class EventFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "title": "Test Event",
            "description": "Test description",
            "startTime": datetime.now(),
            "endTime": datetime.now() + timedelta(hours=1),
        }
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            "title": "Test Event",
            "description": "Test description",
            "startTime": datetime.now(),
            "endTime": datetime.now() - timedelta(hours=1),
        }
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("End time must be after the start time.", form.errors["__all__"])


class ImportICSFormTest(TestCase):
    def test_valid_form(self):
        file_content = b"Valid ICS file content"
        ics_file = SimpleUploadedFile(
            "test.ics", file_content, content_type="application/octet-stream"
        )
        form_data = {"ics_file": ics_file}
        form = ImportICSForm(data={}, files=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_no_file(self):
        form_data = {}
        form = ImportICSForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["ics_file"])

    def test_invalid_form_invalid_file_type(self):
        form_data = {"ics_file": SimpleUploadedFile("test.txt", b"Invalid content")}
        form = ImportICSForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["ics_file"])
