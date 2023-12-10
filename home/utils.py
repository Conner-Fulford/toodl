from django.core.mail import send_mail

def send_event_reminder(event):
    subject = f"Reminder: {event.title}"
    message = f"Hello, this is a reminder about your upcoming event: {event.title} on {event.startTime}"
    recipient_list = [event.user.email]  # Assuming 'user' is a field in your 'Event' model
    send_mail(subject, message, 'from@example.com', recipient_list)
