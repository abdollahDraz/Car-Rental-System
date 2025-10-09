import os

class Vehicle :
  def __init__(self , name , National_ID  ):
    self._set_customer_detials(name , National_ID)

  def calc_cost (self ):
        pass

  def _set_customer_detials (self , Customer_name , National_ID) :
     self._name = Customer_name
     self._National_ID = National_ID


class Car (Vehicle):
    def __init__(self , name , id ):
      super().__init__(name , id)
      self.__menu = {
             "Toyota" : ["Corolla", "Camry", "Yaris"],
             "Honda" : ["Civic", "Accord", "CR-V"],
             "Hyundai" : ["Elantra", "Tucson", "Sonata"],
             "Nissan" : ["Altima", "Sentra", "X-Trail"],
             "BMW" : ["3 Series", "5 Series", "X5"],
             "Mercedes": ["C-Class", "E-Class", "GLC"]
      }
      self.__price_for_one_day = {
          "Toyota" : [2600,2650 , 2800] ,
          "Honda" : [2200,2250 , 2890] ,
          "Hyundai" : [2550,2500 , 2890] ,
          "Nissan" : [2800,2750 , 2650] ,
          "BMW" :[ 2750,2700 , 2650] ,
          "Mercedes" : [2100,2300, 2400]
      }
      self.__state = {
          "Toyota" : [True , True , True],
          "Honda" : [True , True , True],
          "Hyundai" : [True , True , True],
          "Nissan" : [True , True , True],
          "BMW" : [True , True , True],
          "Mercedes" : [True , True , True],
      }
      print(self.__menu)

    def rent_vehicle(self, company, model, days):
        self.__company = company
        self.__model = model
        self.__days = days
        self.__the_Rent = None
        if self.__company not in self.__price_for_one_day:
            print("Error: Company not found, please try again.")
            return   # for break code
        if self.__model not in self.__menu[self.__company]:
            print("Error: Model not found in this company, please try again.")
            return  # for break code
        self.__index = self.__menu[self.__company].index(self.__model)
        if self.__state[self.__company][self.__index] == True:
            self.__state[self.__company][self.__index] = False
            self.__the_Rent = True
            print("Vehicle rented successfully! ")
        else:
            self.__the_Rent = False
            print("the Vehicle is not available ")



    def calc_cost (self ):
            self.__pay = False
            if self.__the_Rent == True :
                self.__price = self.__price_for_one_day[self.__company][self.__index] *self.__days
                print(f"the price of your vehicle  {self.__menu[self.__company][self.__index]}  is :- {self.__price}")
                self.__pay = True
                print("To pay, enter your card")
                f = open("Rentals.txt", "a")
                f.write(
                    f"Customer  name : {self._name}\n"
                    f"National ID :-  {self._National_ID}\n"
                    f"Vehicle :- Car\n"
                    f"Company :- {self.__company}\n"
                    f"Model :- {self.__model}\n"
                    f"Day :- {self.__days}\n"
                    f"price :- {self.__price}\n"
                )
                f.close()
                os.startfile("Rentals.txt")
    def return_vehicle(self ):
        if self.__pay == True :
            self.__state[self.__company][self.__index] = True
            print("You have returned the vehicle You rented. ")



class  Trucks (Vehicle):
    def __init__(self ,name , id ):
     super().__init__(name , id)
     self.__menu = {
         "Ford": ["F-150", "Ranger", "Super Duty"],
         "Chevrolet": ["Silverado", "Colorado"],
         "Ram": ["1500", "2500"],
         "Isuzu": ["D-Max", "N-Series"],
         "Toyota": ["Hilux", "Tundra"]
     }
     self.__price_for_one_day = {
         "Ford" : [1500 , 1550 , 1600],
         "Chevrolet" : [1800 , 1850],
         "Ram" : [2750 , 2700],
         "Isuzu" : [2890 , 2800],
         "Toyota" : [1100 , 1150],
     }
     self.__state = {
         "Ford" : [True , True , True],
          "Chevrolet" : [True , True , True],
         "Ram" : [True , True , True],
         "Isuzu" : [True , True , True],
         "Toyota" : [True , True , True],
     }
     print (self.__menu)

    def rent_vehicle(self, company, model, days):
        self.__company = company
        self.__model = model
        self.__days = days
        self.__the_Rent = None
        if self.__company not in self.__price_for_one_day:
            print("Error: Company not found, please try again.")
            return   # for break code
        if self.__model not in self.__menu[self.__company]:
            print("Error: Model not found in this company, please try again.")
            return  # for break code
        self.__index = self.__menu[self.__company].index(self.__model)
        if self.__state[self.__company][self.__index] == True:
            self.__state[self.__company][self.__index] = False
            self.__the_Rent = True
            print("Vehicle rented successfully! ")
        else:
            self.__the_Rent = False
            print("the Vehicle is not available ")



    def calc_cost (self ):
            self.__pay = False
            if self.__the_Rent == True :
                self.__price = self.__price_for_one_day[self.__company][self.__index] *self.__days
                print(f"the price of your vehicle  {self.__menu[self.__company][self.__index]}  is :- {self.__price}")
                self.__pay = True
                print("To pay, enter your card")
                f = open("Rentals.txt", "a")
                f.write(
                 f"Customer  name : {self._name}\n"
                 f"National ID :-  {self._National_ID}\n"
                 f"Vehicle :- Truck\n"
                 f"Company :- {self.__company}\n"
                 f"Model :- {self.__model}\n"
                 f"Day :- {self.__days}\n"
                 f"price :- {self.__price}\n"
                )
                f.close()
                os.startfile("Rentals.txt")
    def return_vehicle(self ):
        if self.__pay == True :
            self.__state[self.__company][self.__index] = True
            print("You have returned the vehicle You rented. ")


class Bike (Vehicle):
    def __init__(self ,name , id ):
       super().__init__(name , id)
       self.__menu= {
           "Yamaha": ["R15", "MT-15", "FZ"],
           "Honda": ["CBR500R", "CB125R", "Gold Wing"],
           "Suzuki": ["Hayabusa", "Gixxer", "GSX-R750"],
           "Kawasaki": ["Ninja 300", "Z650", "Versys 650"]
       }
       self.__price_for_one_day = {
           "Yamaha": [120 , 125 , 130 ],
           "Honda": [133 , 138 , 124],
           "Suzuki": [138 , 140 , 160],
           "Kawasaki": [199.99, 150 , 180]
       }
       self.__state = {
           "Yamaha" : [True , True , True],
           "Honda" : [True , True , True],
           "Suzuki" : [True , True , True],
           "Kawasaki" : [True , True , True],
       }
       print(self.__menu)


    def rent_vehicle(self, company, model, days):
        self.__company = company
        self.__model = model
        self.__days = days
        self.__the_Rent = None
        if self.__company not in self.__price_for_one_day:
            print("Error: Company not found, please try again.")
            return   # for break code
        if self.__model not in self.__menu[self.__company]:
            print("Error: Model not found in this company, please try again.")
            return  # for break code
        self.__index = self.__menu[self.__company].index(self.__model)
        if self.__state[self.__company][self.__index] == True:
            self.__state[self.__company][self.__index] = False
            self.__the_Rent = True
            print("Vehicle rented successfully! ")
        else:
            self.__the_Rent = False
            print("the Vehicle is not available ")



    def calc_cost (self ):
            self.__pay = False
            if self.__the_Rent == True :
                self.__price = self.__price_for_one_day[self.__company][self.__index] *self.__days
                print(f"the price of your vehicle  {self.__menu[self.__company][self.__index]}  is :- {self.__price}")
                self.__pay = True
                print("To pay, enter your card")
                f = open("Rentals.txt", "a")
                f.write(
                    f"Customer  name : {self._name}\n"
                    f"National ID :-  {self._National_ID}\n"
                    f"Vehicle :- Bike\n"
                    f"Company :- {self.__company}\n"
                    f"Model :- {self.__model}\n"
                    f"Day :- {self.__days}\n"
                    f"price :- {self.__price}\n"
                )
                f.close()
                os.startfile("Rentals.txt")
    def return_vehicle(self ):
        if self.__pay == True :
            self.__state[self.__company][self.__index] = True
            print("You have returned the vehicle You rented. ")



c = Car("Abdollah Mohammed", 30405048801018)
c.rent_vehicle("Toyota", "Corolla", 3)
c.calc_cost()
c.return_vehicle()
