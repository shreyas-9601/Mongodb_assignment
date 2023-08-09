from Orders_model import OrdersModel
from Process_orders_data import Order

class UpdateOrder:
    
    def update_orders(self):
        orders=OrdersModel.objects
        
        for order in orders:
            neworder=Order(order.order_id,order.name,order.birthday,order.email,order.state,order.zipcode)
            order.isvalid=neworder.validate_orders()
            if(order.isvalid):
                OrdersModel.objects(order_id=order.order_id).update_one(set__isvalid=True)

if __name__=='__main__':                
    updateorder = UpdateOrder()
    updateorder.update_orders()