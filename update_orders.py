from orders_model import OrdersModel
from process_orders_data import Order

class UpdateOrder:
    
    def update_orders(self):
        orders=OrdersModel.objects
        
        for order in orders:
            neworder=Order(order.order_id,order.name,order.birthday,order.email,order.state,order.zipcode)
            neworder.mark_as_valid()
        print('All orders updated to database successfully')

if __name__=='__main__':                
    updateorder = UpdateOrder()
    updateorder.update_orders()