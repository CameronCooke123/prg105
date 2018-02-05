"""

    a program that utilizes loops to display the amount of calories burned for
    different amounts of times on a treadmill.

"""

CALORIES_PER_MINUTE = 4.2

minutes_on_treadmill = 10

while minutes_on_treadmill <= 30:
    calories_burned = str(minutes_on_treadmill * CALORIES_PER_MINUTE)
    print("The calories burned in " + str(minutes_on_treadmill) + " minutes are: " + calories_burned)
    minutes_on_treadmill += 5;
