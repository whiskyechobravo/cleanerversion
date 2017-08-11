from django.utils import timezone


def get_utc_now():
    return timezone.now()
