from src import booking_search
from src import constants

if __name__ == "__main__":
    for city in constants.CITIES:
        booking_search = booking_search.BookingSearch(city)
        booking_search.start_search()
