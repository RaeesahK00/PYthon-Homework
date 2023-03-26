print("Task 1")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

add = num1+num2+num3
sub = num1-num2-num3
multiply = num1*num2*num3

print("this is the addition of all numbers: ", add)
print("This is the subtraction of all numbers: ", sub)
print("This is the multiplication: ", multiply)

print(" ")

print("Task 2")
print("Name", "Is", "James", sep="**")

print(" ")

print("Task 3")
num = 8
oct_num = oct(num)[2:]
print("Conversion of decimal {} into octal is {}".format(oct_num, num))

print(" ")

print("Task 4")
num_list = []
print("enter 5 integer numbers:")
for i in range(5):
    num4 = int(input())
    num_list.append(num4)

print("The entered list of integer numbers", num_list)

print(" ")

print("Task 5")

list_one = [2, 6, 9, 12, 14, 18]
list_two = [4, 8, 12, 11, 20, 25, 28]

odd_list_one = list_one[1::2]
even_list_two = list_two[::2]

print("Element at odd-index positions from list one")
print(odd_list_one)

print("Element at odd-index positions from list one")
print(even_list_two)

list_three = odd_list_one + even_list_two

print("Printing final third list")
print(list_three)

print(" ")

print("Task 6")
string = input("Enter a string: ")

if string[:2] == "Is":
    new_string = string
else:
    new_string = "Is" + string

print("The new string is: ", new_string)
print(" ")
