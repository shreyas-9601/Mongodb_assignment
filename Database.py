from mongoengine import *

connect("ordersdb")

class OrderMongodb(Document):   
    order_id = StringField(required=True)
    name = StringField(required=True)
    birthday = StringField(required=True)
    email = StringField(required=True)
    state = StringField(required=True)
    zipcode = StringField(required=True)
    isvalid = BooleanField(default=False)