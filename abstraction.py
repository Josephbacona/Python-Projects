from abc import ABC, abstractmethod
class car (ABC):
    def paySlip(self, amount):
        print("Your puchase amount: ",amount)
#this function is tell us to pass in an argument, but we won't tell you or what kind
#of data it will be.
        @abstractmethod
        def payment(self, amount):
            pass

class DebitCardPayment(car):
#here we'be defined how to implement the patment funcion from its parent paySlip class.
    def payment(self, amount):
        print('Your purchase amount of {} exceeded you $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")
