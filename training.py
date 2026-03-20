a = input("Enter Your Name: ")
print("My name is", a)

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
add = num1+num2
sub = num1-num2
product = num1*num2
divide = num1/num2
module = num1//num2
print("Addition of", num1, "&", num2, "is", add)
print("Subtraction of", num1, "&", num2, "is", sub)
print("Multiplication of", num1, "&", num2, "is", product)
print("Divide of", num1, "&", num2, "is", divide)
print("Module of", num1, "&", num2, "is", module)


age = int(input("Enter Your Age: "))
if age < 13:
    print("You are child")
elif age < 20 :
    print("You are Teenager")
elif age >= 60 :
    print("You are Senior Citizen")
else :
    print("You are Adult")

color = input("Enter the colour of banana: ")
if color == "green" :
    print("Banana is Unripe")
elif color == "yellow" :
    print("Banana is Ripe")
elif color == "brown" :
    print("Banana is overripe")
else :
    print("Invalid Colour Details")    


#FUNCTIONS IN PYTHON
def multiply(a1,a2):
    return a1*a2

print(multiply(5,5))


def user_name():
    username = input("Enter Your Name: ")
    print("Hello", username)

user_name()

def my_name():
    print("My Name is Vaibhav !")

def my_age():
    print("My Age is 19")

def my_course():
    print("I'm pursuing B.Tech")

a = input("Ask ABout Me Anything !")
if a == "name" :
    my_name()
if a == "age" :
    my_age()
if a == "course" :
    my_course()


def your_age():
    age = int(input("Enter Your Age: "))
    if age >= 18:
        print("You are officially adult. Now you are eligible for voting & driving")
    else:
        print("You are minor")

print("If you are interested to know about a fact then fill your age below :)")
your_age()



set = {1,2,3,4,5}
print(set)

a = {"1":"a","2":"b","1":"c"}
print(a)


# Write a function multiply that multiplies two number, but also accept and multiply string
def multi(a,b):
    return a*b

print(multi(7,8))
print(multi("hi",8))

a = 3
b = "hi"
if type(a) and type(b) == int:
    print(a*b)
if type(a) or type(b) == str:
    print(a*b)


number = [1,-3,2,-4,5,9,10,-32,-45]
positive_num_count = 0
for no in number :
    if no > 0 :
        positive_num_count += 1

print("final count of positive no. is:",positive_num_count)

#While Loop

i = int(input("Enter the value of i: "))
while (i<38):
    i = int(input("Enter the value of i: "))
    print(i)
if(i>38):
    print("Enter the smaller value of i")
else:
    print("The Loop is Done")    

rows = int(input("Enter Number of Rows: "))

for i in range(rows):
    print(" " * (rows - i - 1), end = "")
    print("*" * (2 * i + 1))

#Print the table of 9. But Skip the 5th iterattion.
for i in range(1,11):
    if i == 5:
        continue
    print(f"9 x {i} = {9*i}")


for i in range(1,11):
    if i == 5:
        continue
    print("9 x",i,"=",(i*9))

j = 0
while (j<10):
    j = j+1
    if j == 5:
        continue
    print("9 x",j,"=",(9*j))

a = int(input("Enter Your Value: "))
if (a<10):
    print("It is a Single Digit Number")
elif(a<100):
    print("It is a Double Digit Number")
elif(a<1000):
    print("It is a Triple Digit Number")
else:
    print("Digits are above three")



#POWER BI
import pandas
import pandas as pd
pd.__version__
df = pd.DataFrame([11,22,33], columns=['Col_Name'])
print(df)
print(type(df))

data = {
    'Name' : ['Madhav','Vishakha','Lalita','Rishabh'],
    'Age' : ['16','17','18','19'],
    'Salary' : ['90000','70000','50000','30000']
}
df = pd.DataFrame(data)
print(df)
df.rename(columns={'Salary': 'Monthly_Salary'}, inplace=True)
print(df)
df.to_csv('Test_data.csv', index = False)
load_df=pd.read_csv('Test_data.csv')
print(load_df)
