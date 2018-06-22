#Q.1- Create a circle class and initialize it with radius.
#Make two methods getArea and getCircumference inside this class.

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
        area = 3.14 * self.radius * self.radius
        print("area of circle with radius %d is %f"%(self.radius,area))

    def getCircumference(self):
        circum = 2 * 3.14 * self.radius 
        print("Circumference of circle with radius %d is %f"%(self.radius,circum))

c1 = Circle(30)
c1.getArea()
c1.getCircumference()

print("\n\n",10*"*")




#Q.2- Create a Student class and initialize it with name and roll number.
#Make methods to :1. Display - It should display all informations of the student.

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def display(self):
        print("name :",self.name)
        print("roll no :",self.roll_no)

st = Student('anshul',2)
st1 = Student('anmol',8)
st.display()
st1.display()

print("\n\n",10*"*")




#Q.3- Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temperature:
    def cToF(self,celsius):
        far = (celsius * 1.8) + 32
        print("conversion from celsius to farenheit:")
        print("celsius: %0.1f°C\nfarenheit: %0.1f°F"%(celsius,far))

    def fToC(self,far):
        celsius = ((far - 32)* 5)/9
        print("conversion from farenheit to celsius:")
        print("farenheit: %0.1f°F\ncelsius: %0.1f°C"%(far,celsius))

celsius = int(input("enter temperature in celsius:"))
ob = Temperature()
ob.cToF(celsius)
far = int(input("enter temperature in farenheit:"))
ob1 = Temperature()
ob1.fToC(far)

print("\n\n",10*"*")




#Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to 1. Display-Display the details.2. Update- Update the movie details.

class MovieDetails:
    def __init__(self,movie_name,artistname,yor,ratings):
        self.movie_name = movie_name
        self.artistname = artistname
        self.yearOfRel = yor
        self.ratings = ratings

    def display(self):
        print("%s by %s is releasing on %d and has ratings of %d*"%(self.movie_name,self.artistname,self.yearOfRel,self.ratings))

    def update(self):
        self.yearOfRel += 1
        print("%s by %s has postponed its release to %d and has ratings of %d*"%(self.movie_name,self.artistname,self.yearOfRel,self.ratings))


ob = MovieDetails('sanju','Rajkumar Hirani',2018,4)
ob.display()
ob.update()

print("\n\n",10*"*")




#Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
#1. Display expenditure and savings 
#2. Calculate total salary
#3. Display salary

class Expenditure:
    def __init__(self,exp,sav):
        self.expenditure = exp
        self.saving = sav

    def display(self):
        print("person expends %dRs and saves %dRs"%(self.expenditure,self.saving))

    def totalSalary(self):
        self.total =self.expenditure + self.saving

    def displaySalary(self):
        print("total salary = %dRs"%(self.total))

ex = Expenditure(20000,5000)
ex.display()
ex.totalSalary()
ex.displaySalary()

print("\n\n",10*"*")











































