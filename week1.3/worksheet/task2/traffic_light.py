"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""
states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input("Enter steps: "))  # read an integer number of steps (>0)
time = 0

state = "red"

for i in range(0, maxtime + 1):
    time = time + 1
    if time <= 4:
        state = "red"
    elif time <= 7:
        state = "red_amber"
    elif time <= 12:
        state = "green"
    elif time <= 14:
        state = "amber"
    else:
        time = 0
    print(f"Time {systime:03} State {state}")
    systime = systime + 1



# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14