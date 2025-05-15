# calculates c-ratings for batteries

while True:
    print()
    c_rating = float(input('enter the battery c-rating : '))
    battery_capacity = float(input('enter the battery capacity in Ah : '))
    calculated_amps = battery_capacity * c_rating
    time_frame = 60/c_rating

    print(f"A battery with a capacity of {battery_capacity}Ah will provide {calculated_amps} Amps for {time_frame} minutes.")