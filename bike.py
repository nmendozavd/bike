class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
            
    def display_info(self):
        print 'Price is $' + str(self.price) + " Max Speed: " + str(self.max_speed) + " Total Miles: " + str(self.miles)

    def ride(self):
        print 'Riding'
        self.miles += 10
        return self

    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
            self.miles -= 5
        return self

Bike1 = Bike(200, 25)
Bike1.ride().ride().ride().reverse().reverse()
Bike1.display_info()