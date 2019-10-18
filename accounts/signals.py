# ''' When a user logged in it receives the signal, then create a customer in the stripe.
# After that it saves the customer stripe id to the database.'''

import stripe

from django.conf import settings
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from accounts.models import UserStripe

from allauth.account.signals import user_signed_up



stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

@receiver(user_signed_up)
def get_or_create_stripe(request, user, **kwargs):
    print(user.email)
    # print(sociallogin)
    
    try:
        user.userstripe.stripe_id
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(email=str(user.email))
        UserStripe.objects.create(user=user, stripe_id=customer.id)
    except:
        pass



