txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#Placeholders
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("Amit",33)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("Aman",38)

print(txt1)
print(txt2)
print(txt3)



#Basic formatting for default, positional and keyword arguments
# default arguments
print("Hello {}, your balance is {}.".format("Aman", 230.2346))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Amit", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Anand", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Atul", blc=230.2346))


#Simple number formatting
# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))



#Number formatting with padding for int and floats
# integer numbers with minimum width
print("{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

# padding for float numbers
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))




#Number formatting for signed numbers
# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))



#Number formatting with left, right and center alignment
# integer numbers with right alignment
print("{:5d}".format(12))

# float numbers with center alignment
print("{:^10.3f}".format(12.2346))

# integer left alignment filled with zeros
print("{:<05d}".format(12))

# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))



#String formatting with padding and alignment
# string padding with left alignment
print("{:5}".format("cat"))

# string padding with right alignment
print("{:>5}".format("cat"))

# string padding with center alignment
print("{:^5}".format("cat"))

# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))


#Truncating strings with format()
# truncating strings to 3 letters
print("{:.3}".format("caterpillar"))

# truncating strings to 3 letters and padding
print("{:5.3}".format("caterpillar"))

# truncating strings to 3 letters,padding and center alignment
print("{:^5.3}".format("caterpillar"))


#Formatting class members using format()

class Person:
    age = 23
    name = "Amit"
print("{p.name}'s age is: {p.age}".format(p=Person()))


#Dynamic formatting using format()
# dynamic string format template
string = "{:{fill}{align}{width}}"

# passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))

# dynamic float format template
num = "{:{align}{width}.{precision}f}"

# passing format codes as arguments
print(num.format(123.236, align='<', width=8, precision=2))





#Type-specific formatting with format() and overriding __format__() method
import datetime
# datetime formatting
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

# complex number formatting
complexNumber = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))

# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print("Amit's age is: {:age}".format(Person()))





