# enter temperature and dewpoint at your location and get the cloud base in feet.
while True:
    print()
    temp = int(input("Enter temperature in °C : "))
    dew_point = int(input("Enter dewpoint temperature in °C : "))

    cloud_base = (temp - dew_point)/2.5 * 1000

    result = f"The cloud base will be at approximately {cloud_base:,.0f}ft."
    print()
    print(result)