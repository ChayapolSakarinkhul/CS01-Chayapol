score = int(input("Enter Score: "))
midterm = int(input("Midterm Score: "))
final = int(input("Final Score: "))
sum = score + midterm + final

if sum < 50:
    print("Grade: F")
elif sum < 55:
    print("Grade: D")
elif sum < 60:
    print("Grade: D+")
elif sum < 65:
    print("Grade: C")
elif sum < 70:
    print("Grade: C+")
elif sum < 75:
    print("Grade: B") 
elif sum < 80:
    print("Grade: B+")
else:
    print("Grade: A")