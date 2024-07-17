from datetime import datetime

class Customer:
    def __init__(self, customerID, name, email, password, phone, createdAt):
        self.customerID = customerID
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.createdAt = datetime.now()

    def __dict__(self):
        
        return{
            "customerID": self.customerID,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "createdAt": self.createdAt.isoformat()

        }

