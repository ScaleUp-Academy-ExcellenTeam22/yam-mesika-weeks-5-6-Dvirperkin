import datetime
import random
import sys


def create_random_date_in_range(start_date, end_date):
    """This function get two Date objects and rand a new Date object
     between the start_date to the end_date.
     @param start_date - A Date object that indicates the start date of the requested range.
     @param end_date - A Date object that indicates the end date of the requested range.
     @return - A Date object that indicates a random date between the start_date to end_date.
     """

    random_date = rand_date(start_date, end_date - start_date)

    if random_date.weekday() == 0:
        print("I have no vinaigrette!")

    return random_date


def rand_date(start_date, date_range):
    """This function gets Date object that indicate the start date and
    a Date object build from difference between start_date to later Date object.
    @param start_date - A Date object that indicates the start date of the requested range.
    @param date_range - A delta between two Date object that give the range from the start date.
    @return - A Date object that indicates a random date in the given range.
    """
    return start_date + datetime.timedelta(days=random.randrange(date_range.days))


def get_date_from_user():
    """This function gets a date from the user and return a Date object that construct
     with the given date. the date format is: YYYY-MM-DD.
     @return - A Date object that indicates the given date by the user.
     """
    return datetime.date.fromisoformat(input("Enter a date (YYYY-MM-DD):"))


if __name__ == '__main__':
    print(create_random_date_in_range(get_date_from_user(), get_date_from_user()))
