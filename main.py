print("Number 1")
a = 1
while a <= 5:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Only natural numbers allowed")
        break
    print(num)
    a = a + 1

print(" ")
print("Number 2")
for b in range(1, 6):
    for c in range(1, b + 1):
        print(c, end=" ")
    print()

print(" ")
print("Number 3")
num1 = int(input("Enter number: "))
add = 0
for i in range(1, num1+1):
    add = add + i
print("If the user entered ", num1, "the output should be ", add)

print(" ")
print("Number 4")
d = int(input("Enter number: "))
for i in range(1, 11):
    print(d*i)
