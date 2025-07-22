# Fleet Usage Tracker
# Author: Áron Domonkos
# Year: 2022

data = []
with open('cars.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        data.append(line)

converted = []
for row in data:
    converted.append([
        int(row[0]),
        str(row[1]),
        str(row[2]),
        int(row[3]),
        int(row[4]),
        int(row[5])
    ])

print('\nFunction 2')
taken_out = []
for row in converted:
    if row[5] == 0:
        taken_out.append(row)
print(f'{taken_out[-1][0]}. day license plate: {taken_out[-1][2]}')

# day_input = int(input('Day: '))
day_input = 4
traffic = []

print(f'Traffic on day {day_input}:')
for row in converted:
    if row[0] == day_input:
        traffic.append(row)

for row in traffic:
    if row[5] == 0:
        row[5] = 'out'
    else:
        row[5] = 'in'

for row in traffic:
    print(f'{row[1]} {row[2]} {row[3]} {row[5]}')

outgoing = []
incoming = []
for row in converted:
    if row[5] == 1:
        incoming.append(row)
    if row[5] == 0:
        outgoing.append(row)

print(f'At the end of the month {len(outgoing) - len(incoming)} cars were not returned.')

print('\nFunction 5')
cars = []
kilometers = []
plates = []

for i in range(len(converted) - 1):
    if converted[i][2] not in cars:
        cars.append(converted[i][2])

cars = sorted(cars)

for plate in cars:
    km_list = []
    for entry in converted:
        if plate == entry[2]:
            km_list.append(entry[4])
    plates.append(km_list)

for km in plates:
    kilometers.append((km[-1] - km[0]))

for plate, km in zip(cars, kilometers):
    print(plate, km)

print('\nFunction 6')
all_trips = []
flattened = []

for plate in cars:
    trip = []
    for entry in converted:
        if plate == entry[2]:
            trip.append([entry[3], entry[4]])
    all_trips.append(trip)

for trip in all_trips:
    for segment in trip:
        flattened.append(segment)

km_differences = []
persons = []

for i in range(len(flattened) - 1):
    if flattened[i][0] == flattened[i + 1][0]:
        diff = flattened[i + 1][1] - flattened[i][1]
        km_differences.append(diff)

for i in range(len(flattened) - 1):
    if flattened[i][0] == flattened[i + 1][0]:
        if flattened[i + 1][1] - flattened[i][1] == max(km_differences):
            persons.append((flattened[i]))

print(f'Longest trip: {max(km_differences)} km, person: {persons[0][0]}')

triplog = []
departures = []
arrivals = []

# plate_input = input('License plate: ')
plate_input = 'CEG304'
for entry in converted:
    if plate_input == entry[2]:
        if entry[5] == 0:
            departures.append(entry)
        else:
            arrivals.append(entry)

with open('log.txt', 'w') as file:
    for d, a in zip(departures, arrivals):
        file.write(f'{d[3]}\t{d[0]}. {d[1]}\t{d[4]} km\t{a[0]}. {a[1]}\t{a[4]} km\n')
    file.write(f'{departures[-1][3]}\t{departures[-1][0]}. {departures[-1][1]}\t{departures[-1][4]} km')