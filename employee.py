"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""




from enum import Enum
class PaymentMethod(Enum):
    MONTHLY = 1
    HOURLY = 2


class Employee:
    def __init__(self, name, payment_method, rate):
        self.name = name
        self.payment_method = payment_method
        self.rate = rate
        self.hours_worked = 0
        self.commission_amount = 0
        self.commission_time = 0
        self.bonus_amount = 0

    def set_commission(self, commission_amount, commission_time):
        self.commission_amount = commission_amount
        self.commission_time = commission_time

    def get_commission(self):
        return self.commission_amount * self.commission_time

    def set_bonus(self, bonus_amount):
        self.bonus_amount = bonus_amount

    def get_bonus(self):
        return self.bonus_amount

    def set_hours_worked(self, hours_worked):
        self.hours_worked = hours_worked

    def get_pay(self):
        # calcualte based on monthly or hourly work
        if self.payment_method == PaymentMethod.MONTHLY:
            # add commission and bonus
            return self.rate + self.get_bonus() + self.get_commission()
        elif self.payment_method == PaymentMethod.HOURLY:
            if self.hours_worked == 0:
                raise ValueError("please enter hours worked")
            return (self.rate * self.hours_worked) + self.get_bonus() + self.get_commission()
        else:
            raise ValueError("Invalid payment method")


    def __str__(self):

        #working monthly: works on a monthly salary of x 
        #if there is any bonus or commission , delete the last dot 
        if self.payment_method == PaymentMethod.MONTHLY:
  
            # if you have the bonus commission 
            if self.get_bonus() > 0:
                return (
                    f"{self.name} works on a monthly salary of {self.rate} and receives a bonus commission of {self.get_bonus()}. "
                    f"Their total pay is {self.get_pay()}."
                )
            
            # monthly and gets a commission 
            elif self.get_commission() > 0:
                return (
                    f"{self.name} works on a monthly salary of {self.rate} and receives a commission for {self.commission_time} contract(s) at {self.commission_amount}/contract. "
                    f"Their total pay is {self.get_pay()}."
                )
            else:
                return (
                    f"{self.name} works on a monthly salary of {self.rate}. "
                    f"Their total pay is {self.get_pay()}."
                )
        else:

            #only gets bonus 
            if self.get_bonus() > 0:
                return (
                    f"{self.name} works on a contract of {self.hours_worked} hours at {self.rate}/hour and receives a bonus commission of {self.bonus_amount}. "
                    f"Their total pay is {self.get_pay()}."
                )
            #only gets commission
            elif self.get_commission() > 0:
                return (
                    f"{self.name} works on a contract of {self.hours_worked} hours at {self.rate}/hour and receives a commission for {self.commission_time} contract(s) at {self.commission_amount}/contract. "
                    f"Their total pay is {self.get_pay()}."
                )
            else:
                return (
                    f"{self.name} works on a contract of {self.hours_worked} hours at {self.rate}/hour. "
                    f"Their total pay is {self.get_pay()}."
                )



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', PaymentMethod.MONTHLY, 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', PaymentMethod.HOURLY, 25)
charlie.set_hours_worked(100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', PaymentMethod.MONTHLY, 3000)
renee.set_commission(200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', PaymentMethod.HOURLY, 25)
jan.set_commission(220, 3)
jan.set_hours_worked(150)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', PaymentMethod.MONTHLY, 2000)
robbie.set_bonus(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', PaymentMethod.HOURLY, 30)
ariel.set_bonus(600)
ariel.set_hours_worked(120)


print(renee)
