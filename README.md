# Fleet Usage Tracker
This program processes vehicle usage logs of a company with 10 cars based on the given monthly record. It determines statistics and generates usage summaries.

## Task Overview
The program processes a `cars.txt` file where each row contains:
- the day (1–30),
- the time (`hh:mm`),
- the license plate (`CEG300`–`CEG309`),
- the driver's ID (500–600),
- the odometer reading,
- and whether it was an exit (`0`) or an entry (`1`).

The program performs the following:

1. Reads and stores the contents of the file.
2. Displays which car was taken out last.
3. Lists the traffic for a user-given day (who, when, and whether exit or entry).
4. Counts how many cars were not returned by the end of the month.
5. Calculates and displays the total distance driven by each car.
6. Identifies the driver who drove the longest distance in a single trip.
7. Generates a usage log (`log.txt`) for a user-given license plate in the specified format.

The program does not check the validity of the input data; it assumes they are correct.

---
Developed by Áron Domonkos, 2022.
