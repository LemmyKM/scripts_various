# vehicle_log_sheet2.py writes 'date', 'destination', 'opening_km', 'closing_km',
# 'total_km', 'petrol_refill', 'private_business' to a '.txt' file for later edit.
# runs in Pythonista3 on iOs.
# extra files needed for a fresh start :
# 1. 'vehicle_log_kilometers.txt' with the car's latest ODO kilometers which serves as the figure for the 'opening_km'.
# 2. 'vehicle_log_totalkm.txt' with the figure '0' inside the file. '0' is the start for the addition of all the trip_km.
#    It sums the trip km's and is the most right column printed on the 'vehicle_log_sheet.txt'.

import time

date = input("\ndate : ")
destination = input("\ndestination : ").title()

with open('vehicle_log_kilometers.txt', mode='r') as file: #read 'vehicle_log_kilometers.txt' to get the ODO opening_km (which are the closing km from the previous trip.)
    km = file.read()
    opening_km = int(km)
        
while True:
    pvt_bus = input("\nPrivate(P) or Business(B)? ").upper()
    if pvt_bus == "P" or pvt_bus == "B":
        break

closing_km = int(input("\nclosing km : "))
with open('vehicle_log_kilometers.txt', mode='w') as file:
    file.write(f"{closing_km}")

trip_km = closing_km - opening_km
try:
    petrol_refill = float(input("\nliters of petrol : "))
except ValueError:
    petrol_refill = float(input("Please enter liters of petrol with a '.' for a decimal instead of ',' : "))


with open('vehicle_log_totalkm.txt', mode='r') as file: # read total km from vehicle_log_sheet and make integer
    total = file.read()
    int_total = int(total)

with open('vehicle_log_totalkm.txt', mode='w') as file: # take total km from above and add trip_km and write to file
    total_end = int_total + trip_km
    file.write(f"{total_end}")

with open("vehicle_log_sheet.txt", mode="a", encoding="utf-8") as log:
        log.write(f"{date:17}{destination:<31}{opening_km:<10,}{pvt_bus:<5}{closing_km:<10,}{petrol_refill:<5.2f}l{trip_km:>5}km{total_end:>7}km\n")

print("\n--> Finished editing the record")

time.sleep(1) # to make printed line 45 visible.
quit() # to properly make pythonista write data to file.