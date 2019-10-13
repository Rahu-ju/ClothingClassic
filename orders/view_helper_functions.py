import uuid
from orders.models import Order


# generate unique order id
def order_id_generator():
    order_id = str(uuid.uuid4())[:11].replace('-', '').lower()
    # checking the order already exist or not
    try:
        Order.objects.get(id=order_id)
        order_id_generator()
    except:
        return order_id

# Another way to genetrate id 
import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in size)
    return the_id