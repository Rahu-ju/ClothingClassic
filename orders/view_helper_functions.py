import uuid
from orders.models import Order


# generate unique order id
def get_order_id():
    order_id = str(uuid.uuid4())[:11].replace('-', '').lower()
    # checking the order already exist or not
    try:
        Order.objects.get(id=order_id)
        get_order_id()
    except:
        return order_id