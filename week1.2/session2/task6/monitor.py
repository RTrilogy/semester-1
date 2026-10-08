# Week 1.2, Session 2: Task 6
temp = int(input("Enter the machine's temperature in degrees Celsius: "))
press = int(input("Enter the machine's pressure in PSI: "))
status = int(input("Enter the machine's operational status (1 for operating, 0 for stopped) (integer): "))
danger = False

if temp > 80:
    print("Temperatures high, shutdown recommended.")
    danger = True
elif temp >= 50 and temp <= 80:
    print("Temperature is within safe limits.")
else:
    print("No actions needed, temperature is low.")

if press > 100:
    print("High pressure detected, maintenance recommended.")
    danger = True
elif press >= 70 and press <= 100:
    print("Pressure is stable.")
else:
    print("No actions needed, low pressure detected.")

if status == 1:
    if danger:
        print("Warning! Computer is running in unsafe conditions. Shutdown recommended.")
    else:
        print("No actions needed, computer is running normally.")
else:
    print("Computer is off, no actions needed.")

record = open("record.txt", "w")
if danger and status == 1:
    record.write(f"{temp}, {press}, {status}, shutdown recommended.\n")
elif status == 0:
    record.write(f"{temp}, {press}, {status}, computer is turned off.\n")
else:
    record.write(f"{temp}, {press}, {status}, no actions needed.\n")