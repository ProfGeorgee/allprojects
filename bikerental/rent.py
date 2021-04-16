'''
Customers can
done 1.See available bikes on the shop
done 2.Rent bikes on hourly basis $5 per hour.
done 3.Rent bikes on daily basis $20 per day.
//4.Rent bikes on weekly basis $60 per week.
//5.Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price.
The bike rental shop can:
//1.issue a bill when customer decides to return the bike.
//2.display available inventory
3.take requests on hourly, daily and weekly basis by cross verifying stock.
For simplicity we assume that:
1.Any customer requests rentals of only one type i.e hourly, monthly or weekly
2.Is free to chose the number of bikes he/she wants.
3.Requested bikes should be less than available stock.
'''
import datetime
class Rent():
    def __init__(self,stock = int(input())):
        self.stock = stock


    def bikes(self):
        print("we currently have {} bikes".format(self.stock))
        return self.stock


    def hourly(self, x):
        if 0:
            print("number has to be positive")
        elif x > self.stock:
            print("not enough bikes in stock")

        else:
            date = datetime.datetime.now()
            print("you took the hourly plan and you rented {} bikes you will also get charged from this time {} until you cancel".format(x,date))
            self.stock -= x
            return date
        

    def daily(self, x):
        if 0:
            print("number has to be positive")
        elif x > self.stock:
            print("not enoug bikes in stock")
        else:
            date= datetime.datetime.now()
            print("started the daily plan on {} with {} bikes,a bill will be issued when you return it".format(date,x))
            return date



    def weekly(self,x):
        if 0:
            print("number has to be positive")
        elif x > self.stock:
            print("not enough bikes in stock")
        else:
            date = datetime.datetime.now()
            print("started the weekly plan on {} with {} bikes, a bill will be issued when you return it".format(date,x))
            return date

    def bikeReturn(self, request):


        rentalTime, rentlaBasis, numofbikes = request, bill = 0
        if rentalTime and rentalBasis and numofbikes:
            self.stock += numofbikes
            date = datetime.datetime.now()
            rentalPeriod = date - rentalTime

            if rentalTime == 1:
                bill = round(rentalPeriod/3600) *5 * numofbikes

            elif rentalTime == 2:
                bill = round(rentalPeriod/3600) * 20 * numofbikes
            elif rentalTime == 3:
                bill = round(rentalPeriod/3600) * 60 * numofbikes

            if(3 <=numofbikes>=5):
                bill = round(rentalPeriod/3600) * 5 * numofbikes
                bill1 = (bill // 10) * 3
                bill -= bill1 
            



class Customer():


    def __init__(self):
        self.bikes = 0
        self.bill = 0
        self.rentalBasis = 0
        self.rentalTime = 0
    def rentBike(self):
        bikes = int(input("how many bikes do you want?"))
        try:
            bikes = int(bikes)
            
        except ValueError:
            print("not a positive integer")
            return -1

        if bikes < 1:
            print("invalid input bikes should be a positive int")
            return -1

        else:
            self.bikes = bikes
        return self.bikes


    def returnbikes(self):
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalBasis and self.rentalTime and self.bikes
        else:
            return 0,0,0



Customer()
Rent()

