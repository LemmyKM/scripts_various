with open('private_km.txt', mode='r') as file, open('business_km.txt', mode='r') as file2, open('vehicle_log_month_totalkm.txt', mode='r') as file3:
    pvt_km = file.read()
    int_pvt_km = int(pvt_km)
    bus_km = file2.read()
    int_bus_km = int(bus_km)
    veh_log_month_total_km = file3.read()
    int_veh_log_month_total_km = int(veh_log_month_total_km)

def calc_percentage():
    pct_pvt_km = int_pvt_km/int_veh_log_month_total_km * 100
    pct_bus_km = int_bus_km/int_veh_log_month_total_km * 100
    print()
    print(f"{pct_pvt_km:.0f}% private km; {pct_bus_km:.0f}% business km.")
    print()
calc_percentage()