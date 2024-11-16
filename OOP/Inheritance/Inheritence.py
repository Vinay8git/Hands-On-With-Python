# class Par:
#     def __init__(self):
#         print("Parents class")
# class Child(Par):
#     pass
#
# obj=Child()

# class Vehicle:
#     def __init__(self,a,b,c):
#         self.__a=a  #Private
#         self._b=b   #Protected
#         self.c=c    #Public
#
# class car(Vehicle):
#     print("Bugatti")
#
# acc=car(10,20,30)
# print(acc.c)
# print(acc._b)
# print(acc._Vehicle__a)

class game:
    def __init__(self, play, pause, stop):
        self.play = play
        self._pause = pause
        self.__stop = stop

user=game(1,2,3)
print(user.__stop) # Error - because stop is a private variable and can be used within class only

print(user._game.__stop)