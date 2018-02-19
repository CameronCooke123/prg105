"""

    a program that calculates the total rainfall and average rainfall per month
    over a user-specified period of time

"""


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
total_rain_fall = 0
number_of_years = int(input("How many years do you have data for?: "))

for year in range(0, number_of_years):
    for month in range(0, 12):
        inches_fell_text = str("How many inches of rain fell in " + months[month] + " of year " + str(year + 1) + "?: ")
        inches_of_rain_this_month = int(input(inches_fell_text))
        total_rain_fall += inches_of_rain_this_month

number_of_months = number_of_years * 12
average_rain_per_month = total_rain_fall / number_of_months  # I'm assuming this is to be a float

print("\nTotal number of months: " + format(number_of_months, '11,'))
print("Total rain fall: " + format(total_rain_fall, '18,') + " in.")
print("Average rain fall per month: " + format(average_rain_per_month, '6,.2f') + " in.")
