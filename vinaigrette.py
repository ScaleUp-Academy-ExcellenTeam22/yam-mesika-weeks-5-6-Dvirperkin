import datetime
import random


def random_date_in_range():
    date1 = input("Enter first date (YYYY-MM-DD):")
    date2 = input("Enter second date (YYYY-MM-DD):")

    try:
        date1 = datetime.date.fromisoformat(date1)
        date2 = datetime.date.fromisoformat(date2)
    except ValueError:
        print("Incorrect date format")
        return

    delta = date2 - date1

    random_date = datetime.date

    try:
        random_date = date1 + datetime.timedelta(days=random.randrange(delta.days))
    except ValueError:
        print("First date must be before second date")

    if random_date.weekday() == 2:
        print("I have not vinaigrette!")

random_date_in_range()
