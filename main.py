# SPDX-License-Identifier: MIT
import re

MIN_CHARGE = 90.0
RATE = 60.0

# Task 1


def printWelcome() -> None:
    print("The Best Cheap Same Day Service.")
    FIRST_NAME = "Lucas"
    SURNAME = "Cullen"
    STUDENT_ID = 123
    print(f"Written by {FIRST_NAME} {SURNAME} n{STUDENT_ID}")


def getHours(question="Number of hours required for the service? ") -> float:
    hours_input = input(question)
    match = re.search(r"[\d.]+", hours_input)
    return float(match.group()) if match else 0.0


# Task 3
def calculateCharge(hours) -> float:
    if hours < 0:
        return MIN_CHARGE

    charge = RATE * hours
    if charge < MIN_CHARGE:
        return MIN_CHARGE

    return charge


printWelcome()

# Task 2
hours = getHours()
charge = calculateCharge(hours)

print(f"Service cost will be ${charge:,.2f}")

NUMBER_OF_JOBS = 6
jobs = []

for i in range(0, NUMBER_OF_JOBS):
    question = f"Number of hours required for service {i + 1}? "
    hours = getHours(question=question)
    jobs.append(hours)

THRESHOLD = 1.5
filtered = list(filter(lambda h: h > THRESHOLD, jobs))
sum = sum(filtered)
count = len(filtered)
longest = max(jobs)
average = sum / count if count > 0 else 0.0

print(f"Sum = {sum}")
print(f"Count = {count}")
print(f"Longest = {longest}")
print(f"Average = {longest}")