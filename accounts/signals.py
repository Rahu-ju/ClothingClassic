# ''' When a user logged in it receives the signal, then create a customer in the stripe.
# After that it saves the customer stripe id to the database.'''

import stripe

from django.contrib.auth.signals import user_logged_in
from django.conf import settings

from accounts.models import UserStripe



stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
def get_or_create_stripe(sender, user, *args, **kwargs):
    try:
        user.userstripe.stripe_id
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(email=str(user.email))
        UserStripe.objects.create(user=user, stripe_id=customer.id)
    except:
        pass
    
user_logged_in.connect(get_or_create_stripe)


