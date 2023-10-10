# import hello

# for i in range(10):
#     print(f"the math of {i} is {hello.square(i)}")

# class point():
#     def __init__(self, input1, input2): 
# # () consists of the arguments
# # self references the object we are currently dealing with
# # init is called auto every time the func is called
#         self.x = input1 #basically we are saying to save x and y separelty in the same objext
#         self.y = input2

# p = point(2,8)
# print(p.x) #calling the x property of p
# print(p.y)


# class Point():
#     def __init__(self, input1,input2):
#         self.x = input1
#         self.y = input2

# p = Point(2,8)
# print(p.x)
# print(p.y)

# # flight program
# class Flight():
#     def __init__(self, capacity): #creating a class
#         self.capacity = capacity #defining where to store the capacity
#         self.passengers = []    #creating a list to store the passengers

#     def add_passenger(self, name): #defining a function to add the passengerds
#         if not self.open_seats():  # this basicallly mezans if openseats==0
#             return False 
#         self.passengers.append(name) #since we usin return true and return false, it isnt really needed to use if else
#         return True

#     def open_seats(self): 
#         return self.capacity - len(self.passengers) # checking the capacity of the flight


# flight = Flight(3) #creating an object

# people = ["B", "c", "d", "e"]  #input
# for person in people:
#     if flight.add_passenger(person):
#         print(f"Added {person} to the flight successfully")
#     else:
#         print(f"No available seats for {person}")


