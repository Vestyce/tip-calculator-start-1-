#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Tip Calculator")
bill = float(input("What is the total bill?: $"))
tippercentage = int(input("What precentage tip you want to give? 10,12, or 15?: "))
people = int(input("How many people to split the bill?: "))

#Initial percentage calculations
# percent = tippercentage * .01
# percentagetip = percent + 1.00
# perperson = ( bill / people ) * percentagetip
# Another way to calculate tips can be:
total_bill = ( ( tippercentage / 100 ) * bill ) + bill
perperson = total_bill / people

#print("Each person pays: " + "$" + str(round(perperson, 2)))
#f'{value:{width}.{precision}}'
print(f"Each person pays ${perperson:.2f}")

#Another way to format:
#final_amount = "{:.2f}".format(perperson)
