from django.contrib.auth.models import User
from django.db.models.signals import post_save
# token is another table which pretty much 
# just connects a user and the token itself
from rest_framework.authtoken.models import Token


# ensures that every new registered user 
# get an unique token
def set_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


post_save.connect(set_user_token, sender=User)