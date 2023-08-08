from Database import OrderMongodb
from Python_assignment import Order

class UpdateOrder:
    
    def update(self):
        orders=OrderMongodb.objects
        
        for order in orders:
            neworder=Order(order.order_id,order.name,order.birthday,order.email,order.state,order.zipcode)
            order.isvalid=neworder.validate_orders()
            if(order.isvalid):
                OrderMongodb.objects(order_id=order.order_id).update_one(set__isvalid=True)

if __name__=='__main__':                
    updateorder = UpdateOrder()
    updateorder.update()