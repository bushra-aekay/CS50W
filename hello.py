# name = input("name:")
# print(f"hello {name}")
# houses = {"harry": "gryffindor", "draco": "slytherin"} #dict
# print(houses["harry"]) #dict word --> index 
# houses["hermoine"] = "gryffindor" #adds to the dict

# def square(x,):
#     return x * x

# for i in range(10):
#     print(f"the math of {i} is {square(i)}")

class Flight():
    def _init(self, capacity):
        self.capacity = capacity   #self.capacity is not same as the one defined in arg
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)