from abc import ABC, abstractmethod
import math
import random
class Reservation(ABC):
    @abstractmethod
    def check_in(self):
        pass
    @abstractmethod
    def confirmation(self):
        pass
    @abstractmethod
    def ticket(self):
        pass
class Train(Reservation):
    def __init__(self):
        self.quota=dict()
        self.name=""
        self.age=0
        self.frm=""
        self.to=""
    def check_in(self):
        print("Welcome To Indian Railways!")
        print("Please enter your deatils")
        self.name=input("Enter your name: ")
        self.age=int(input("Enter your age: "))
        self.frm=input("Enter from: ")
        self.to=input("Enter to: ")
        if self.frm not in self.quota:
            self.quota[self.frm]=0
        else:
            self.quota[self.frm]+=1


    def confirmation(self):
        if self.quota[self.frm] >= 10:
            print("Waiting")
        else:
            print("Confirmed")
            self.ticket(True)

    def ticket(self, can_book=False):
        if can_book:
            print("Your Ticket")
            print("Ticket Number:",random.random()*100000000000000000)
            print("Name:"+self.name+"  Age:",self.age)
            print("Boogey Number:" ,random.randint(1,50))
            print("Seat Number:" ,random.randint(1,35))
            print("From:"+self.frm+"  To:"+self.to)


class Airplane(Reservation):
    def check_in(self):
        pass
    def confirmation(self):
        pass
    def ticket(self):
        pass
    

train=Train()
train.check_in()
train.confirmation()