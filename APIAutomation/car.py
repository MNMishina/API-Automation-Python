class Car:
    def __init__(self, model, year, engine, price, mileage):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def car_info(self):
        info = ("Car model: " + self.model + ", Year " + str(self.year) + ", Engine " + self.engine + ", Price " +
                str(self.price)) + ", Vehicle mileage " + str(self.mileage)
        print(info)

    def get_wheels_quantity(self):
        print("Wheels quantity is: " + str(self.wheels))

    def update_wheels(self, p):
        self.wheels = p


truck = Car("MAN", 2008, "V8", 1200, 1648)
# truck.car_info()
# truck.update_wheels(8)
# truck.get_wheels_quantity()
