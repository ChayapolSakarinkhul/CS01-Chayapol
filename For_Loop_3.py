number = int(input("Enter Number: "))
count = 0
for i in range(number):
    if i % 2 == 1:
        count += 1
        print(i)
