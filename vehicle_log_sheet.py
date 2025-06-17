# vehicle_log_sheet2.py writes 'date', 'destination', 'opening_km', 'closing_km',
# 'total_km', 'petrol_refill', 'private_business' to a '.txt' file for later edit.

date = input("\ndate : ")
destination = input("\ndestination : ")
opening_km = int(input("\nopening km : "))
while True:
    pvt_bus = input("\nPrivate(P) or Business(B)? ").upper()
    if pvt_bus == "P" or pvt_bus == "B":
        break
closing_km = int(input("\nclosing km : "))
total_km = closing_km - opening_km
try:
    petrol_refill = float(input("\nliters of petrol : "))
except ValueError:
    petrol_refill = float(input("Please enter liters of petrol with a '.' for a decimal instead of ',' : "))

print("\n--> Finished editing the record")

with open("vehicle_log_sheet.txt", mode="a", encoding="utf-8") as log:
        log.write(f"{date:17}{destination:<35}{opening_km:<10,}{pvt_bus:<5}{closing_km:<10,}{petrol_refill:<5.2f}l{total_km:>5}km\n")
