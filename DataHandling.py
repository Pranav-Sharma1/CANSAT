from PressureTest import *

import csv

with open('data.csv', 'a', newline='') as csvfile:
    fieldnames = ['timestamp', 'altitude', 'temperature', 'pressure']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header if the file is empty
    if csvfile.tell() == 0:
        writer.writeheader()

    # Write data
    writer.writerow({'timestamp': int(time.time()), 'altitude': altitude, 'temperature': temp, 'pressure': pressure })