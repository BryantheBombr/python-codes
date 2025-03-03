print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
#Calculate the extra amount that will be paid

#Make sure that the tip is one of the specific amounts shown
try:
    if tip == 10,12,15:

    else:
        print("The tip must be 10%, 12% or 15% of the bill")
except ValueError:
    print("The tip must be 10%, 12% or 15% of the bill")

people = int(input("How many people to split the bill? "))
#Find out the number of people that would pay

#Start by finding the total amount
total = extra + bill

#Then divide the total amount by the number of people
final = total/people

print("Everyone should pay " + round(final, 2))