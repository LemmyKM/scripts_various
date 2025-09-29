# vehicle_log_sheet.py writes 'date', 'destination', 'opening_km', 'closing_km',
# 'total_km', 'petrol_refill', 'private_business' to 'vehicle_log_sheet.txt' file for later edit.
# runs in Pythonista3 on iOs.
# extra files needed for a fresh start at the beginning of every month:
# 1. 'vehicle_log_odo_kilometers.txt' with the car's latest ODO kilometers which serves as the figure for the 'opening_km'.
# 2. 'vehicle_log_month_totalkm.txt' with the figure '0' inside the file. '0' is the start for the addition of all the trip_km.
#    It sums the trip km's and is the most right column printed on the 'vehicle_log_sheet.txt'.
# 3. 'business_km.txt' with the figure '0' inside the file.
# 4. 'private_km.txt' with the figure '0' inside the file.
# 5. 'calculate_percentage_pvt_business.py' is optional and calculates the percentage of km between business and private.

import time

date = input("\ndate : ")
destination = input("\ndestination : ").title()
        
while True:
    pvt_bus = input("\nPrivate(P) or Business(B)? ").upper()
    if pvt_bus == "P" or pvt_bus == "B":
        break

with open('vehicle_log_odo_kilometers.txt', mode='r') as file: #read 'vehicle_log_odo_kilometers.txt' to get the ODO opening_km (which are the closing km from the previous trip.)
    odo_km = file.read()
    opening_km = int(odo_km)

closing_km = int(input("\nclosing km : "))
with open('vehicle_log_odo_kilometers.txt', mode='w') as file:
    file.write(f"{closing_km}")

trip_km = closing_km - opening_km

def private_business_km():
    if pvt_bus == "P":
        with open('private_km.txt', mode='r') as file:
            pvt_km = file.read()
            int_pvt_km = int(pvt_km)
            add_trip_km_to_file_p = trip_km + int_pvt_km
        with open('private_km.txt', mode='w') as file:
            file.write(f"{add_trip_km_to_file_p}")
    else:
        with open('business_km.txt', mode='r') as file:
            bus_km = file.read()
            int_bus_km = int(bus_km)
            add_trip_km_to_file_b = trip_km + int_bus_km
        with open('business_km.txt', mode='w') as file:
            file.write(f"{add_trip_km_to_file_b}")

private_business_km()

try:
    petrol_refill = float(input("\nliters of petrol : "))
except ValueError:
    petrol_refill = float(input("Please enter liters of petrol with a '.' for a decimal instead of ',' : "))

# calculates the total monthly km after every trip
with open('vehicle_log_month_totalkm.txt', mode='r') as file: # READ monthly total km from vehicle_log_month_totalkm.txt and make integer
    total = file.read()
    int_total = int(total)
with open('vehicle_log_month_totalkm.txt', mode='w') as file: # take total km from above (int_total) and add trip_km and WRITE to file
    total_end = int_total + trip_km
    file.write(f"{total_end}")

with open("vehicle_log_sheet.txt", mode="a", encoding="utf-8") as log:
        log.write(f"{date:17}{destination:<27}{opening_km:<10,}{pvt_bus:<4}{closing_km:<10,}{petrol_refill:<5.2f}l{trip_km:>5}km{total_end:>7}km\n")

print("\n--> Finished editing the record")

time.sleep(1) # to make printed line 66 visible.
quit() # to properly make pythonista write data to file.