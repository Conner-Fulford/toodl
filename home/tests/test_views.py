from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from home.models import Event, CustomUser


class CalendarViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username="testuser", password="testpass"
        )
        self.client.login(username="testuser", password="testpass")

    def test_calendar_view(self):
        response = self.client.get(reverse("calendar"))
        self.assertEqual(response.status_code, 200)

    def test_get_events_view(self):
        response = self.client.get(reverse("get_events"))
        self.assertEqual(response.status_code, 200)

    def test_export_events_view(self):
        event = Event.objects.create(
            user=self.user,
            title="Test Event",
            description="Event description",
            startTime=timezone.now(),
            endTime=timezone.now() + timezone.timedelta(hours=1),
        )
        response = self.client.get(reverse("export_events"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("BEGIN:VCALENDAR", str(response.content))

    def test_delete_event_view(self):
        event = Event.objects.create(
            user=self.user,
            title="Test Event",
            description="Event description",
            startTime=timezone.now(),
            endTime=timezone.now() + timezone.timedelta(hours=1),
        )
        response = self.client.post(
            reverse("delete_event", args=[event.id]), {"event_id": event.id}
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Event.objects.filter(pk=event.id).exists())

    def test_import_events(self):
        ics_content = b"BEGIN:VCALENDAR\nBEGIN:VEVENT\nSUMMARY:Test Event\nDTSTART:20230101T120000\nDTEND:20230101T130000\nEND:VEVENT\nEND:VCALENDAR"
        ics_file = SimpleUploadedFile(
            "test.ics", ics_content, content_type="text/calendar"
        )
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse("import_events"), {"ics_file": ics_file})
        self.assertEqual(response.status_code, 302)

    def test_login_view(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
