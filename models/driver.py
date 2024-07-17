from datetime import datetime

class Driver:
    def __init__(self, driverID, name, email, password, phone, createdAt):
        self.driverID = driverID
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.createdAt = datetime.now()

    def __dict__(self):
        
        return{
            "driverID": self.driverID,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "createdAt": self.createdAt.isoformat()

        }