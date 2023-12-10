from datetime import datetime, timedelta
from celery import shared_task
from .models import Event  # Import your Event model
from .utils import send_event_reminder  # Import the send_event_reminder function

@shared_task
def check_for_upcoming_events():
    now = datetime.now()
    one_day_from_now = now + timedelta(days=1)

    # Query to find events happening within the next day
    upcoming_events = Event.objects.filter(startTime__gte=now, startTime__lte=one_day_from_now)

    for event in upcoming_events:
        send_event_reminder(event)



# from celery import shared_task
# from .models import Event
# from datetime import datetime, timedelta
# from .utils import send_event_reminder

# @shared_task
# def check_for_upcoming_events():
#     now = datetime.now()
#     upcoming_events = Event.objects.filter(startTime__lte=now + timedelta(days=1))  # Adjust as needed
#     for event in upcoming_events:
#         send_event_reminder(event)
