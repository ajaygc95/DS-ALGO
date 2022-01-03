from engine import Engine
class Car:

    def __init__ (self):
        print("car started")


    def reverse(self, parameter):
        print("this is ", parameter)
        for i in range(0,5):
            print(i)

    engine_v6 = Engine()



class Snake:

    def __init__ (self):
        pass


    def reverse(self, parameter):
        for i in range(0,5):
            print(i)


car_camaro_black = Car()
car_camaro_black.reverse("silver")


car_camaro_white = Car()
car_camaro_white.reverse("white")
