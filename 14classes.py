# class class_name(other_class -> optional):
#   def __init__(self, inputs):
#       self.inputs = inputs
#   other_function and do somthing

class car:
    def __init__(self, speed, price):
        self.speed = speed
        self.price = price

    def show_speed(self):
        print (self.speed)
    def show_price(self):
        print (self.price)

car1 = car(200,  15) 
car1.show_speed()
car1.show_price()

print ('-----------')


class moderCar(car):
    def __init__(self, speed, price, door_num, battery_status):
        self.speed = speed
        self.price = price
        self.door = door_num
        self.battey = battery_status
    
    def show_speed(self):
        print (f"Speed: {self.speed}")
    def show_door(self):
        print (self.door)
    def show_battery(self):
        print (self.battey)

car2 = moderCar(200, 15, 4, 'good')
car2.show_speed()
car2.show_price()
car2.show_door()
car2.show_battery()