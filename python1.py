
name = input("Enter student name: ")
dob = input("Enter date of birth (DD/MM/YYYY): ")
reg_no = input("Enter registration number: ")
time = input("Enter default time: ")
marks = []
for i in range(1, 6):
    m = int(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

print("\n--- Student Details ---")
print("Name:", name)
print("DOB:", dob)
print("Registration Number:", reg_no)
print("Default Time:", time)
print("Marks:", marks) 
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Message: Excellent Performance!")
elif percentage >= 75:
    print("Message: Very Good!")
elif percentage >= 50:
    print("Message: Pass")
else:
    print("Message: Fail")