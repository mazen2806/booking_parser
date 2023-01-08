from bs4 import BeautifulSoup

from src.models import hotel


class PropertyParser:
    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        container = soup.select('div[data-testid="property-card"]')

        properties = []
        for el in container:
            h = hotel.Hotel()

            hotel_name_el = el.select('div[data-testid="title"]')
            if hotel_name_el:
                h.name = hotel_name_el[0].text

            hotel_href_el = el.select('a[data-testid="title-link"]')
            if hotel_href_el:
                attrs = hotel_href_el[0].attrs
                h.details_url = attrs['href'] if 'href' in attrs else ''

            hotel_stars_el = el.select('div[data-testid="rating-stars"] span')
            if hotel_stars_el:
                h.stars_count = len(hotel_stars_el)

            hotel_squares_el = el.select('div[data-testid="rating-squares"] span')
            if hotel_squares_el:
                h.stars_count = len(hotel_squares_el)

            # hotel_price_el = el.select('span[data-testid="price-and-discounted-price"]')
            # if hotel_price_el:
            #     h.price = hotel_price_el[0].text

            if hotel_stars_el:
                attrs = hotel_href_el[0].attrs
                h.details_url = attrs['href'] if 'href' in attrs else ''

            hotel_score_el = el.select('div[data-testid="review-score"]')
            if hotel_score_el:
                h.score = hotel_score_el[0].next.text if hotel_score_el[0].next else ''
            if h.score and h.name:
                properties.append(h)

        return properties
