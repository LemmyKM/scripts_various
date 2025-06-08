# vehicle log sheet
import pandas as pd
import numpy as np

data = {
    'Date': ['10 mei 1940', '15 augustus 1945'],
    'Destination': ['Bommerskonten', 'Praag'],
    'Opening_km': [110, 156],
    'Closing_km': [145, 189]
}

choice = input("\nDo you want to create a document? (y/n) : ")
if choice.lower() == "n":
    date = input("\nenter the date : ")
    data['Date'].append(date)

    destination = input("\nenter destination : ")
    data['Destination'].append(destination)

    opening_km = input("\nenter opening km : ")
    data['Opening_km'].append(opening_km)

    closing_km = input("\nenter closing km : ")
    data['Closing_km'].append(closing_km)

else:
    table = pd.DataFrame(data)
    print(table)


