class Train:

    def __init__(self, train_number):
        self.train_number = train_number


    def book_ticket(self, frm, to):
        print(f"Your ticket for train {self.train_number} from {frm} to {to} has been booked successfully.")

    
    def get_status(self):
        print("Your train is on time.")

    
    def fare_info(self, frm, to):
        print(f"The fare for the train from {frm} to {to} is $50.")


t1 = Train("12345")
t1.book_ticket("New York", "Los Angeles")
t1.get_status()
t1.fare_info("New York", "Los Angeles")