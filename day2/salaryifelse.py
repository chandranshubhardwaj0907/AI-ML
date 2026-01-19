# Write a program that takes as input. Using conditional statements, calculate the final tax rate based on these rules:
# •
# If salary < 30,000 → 5%
# •
# If salary is 30,000–70,000 → 15%
# •
# If salary > 70,000 → 25%

salary = float(input("Enter your salary: "))

if salary <30000:
    tax = 0.05*salary
elif 30000 <= salary < 70000:
    tax = 0.15*salary
else:
    tax = 0.25*salary

print(f"The tax on your {salary} is:", tax)    
