
from .models import AuthToken
from django.utils import timezone
from datetime import timedelta
from .serializers import AuthTokenSerializer

def get_user_token(session_id):
    token = AuthToken.objects.filter(user = session_id)
    if token.exists():
        return token[0]
    else:
        return None

def update_token(session_id, acces_token,token_type, expires_in, refresh_token):
    token = get_user_token(session_id)
    expires_in = timezone.now() + timedelta(second=expires_in)
    