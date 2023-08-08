import csv
from Database import OrderMongodb
        
        
class InsertToMongodb:
    
    
    def insert(self):
        with open('orders.csv', 'r') as file:
            csvreader = csv.reader(file)
            headers = next(csvreader)

            id_index = headers.index('ID')
            name_index = headers.index('Name')
            birthday_index = headers.index('Birthday')
            email_index = headers.index('Email')
            state_index = headers.index('State')
            zipcode_index = headers.index('ZipCode')

            for row in csvreader:
                order_id = row[id_index]
                name = row[name_index]
                birthday = row[birthday_index]
                email = row[email_index]
                state = row[state_index]
                zipcode = row[zipcode_index]
                
                order=OrderMongodb(order_id=order_id, name=name, birthday=birthday, email=email, state=state, zipcode=zipcode)
                OrderMongodb.save(order)
                    
if __name__ == '__main__':                  
    inserttomongodb = InsertToMongodb()
    inserttomongodb.insert()