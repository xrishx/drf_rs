from django.core.signals import request_started
from django.dispatch import receiver
from django.utils.timezone import now

@receiver(request_started)
def log_user_visit(sender, environ, **kwargs):
    ip = environ.get('REMOTE_ADDR', 'Unknown IP')
    user_agent = environ.get('HTTP_USER_AGENT', 'Unknown Device')
    current_time = now()

    print(f"[User Visit] IP: {ip} | Device: {user_agent} | Time: {current_time}")
