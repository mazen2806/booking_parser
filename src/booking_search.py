import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from src import property_parser
from src.db import database


class BookingSearch:
    def __init__(self, city):
        self.site_url = 'https://booking.com'
        self.city = city
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.property_parser = property_parser.PropertyParser(self.driver)

    def get_browser_session(self):
        self.driver.get(self.site_url)

    def start_search(self):
        step_methods = [self.get_browser_session, self.set_city, self.set_location, self.set_dates,
                        self.set_adults_count, self.search, self.collect_data_by_page]
        for step in step_methods:
            step()
            time.sleep(2)
        self.driver.close()

    def set_city(self):
        ss_txt = self.driver.find_element(By.ID, 'ss')
        ss_txt.send_keys(self.city)

    def set_location(self):
        location_items = self.driver.find_elements(By.CLASS_NAME, 'sb-autocomplete__item-with_photo')
        time.sleep(2)
        if location_items:
            location_items[0].click()

    def accept_cookies(self):
        time.sleep(3)
        accept_btn = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        accept_btn.click()
        time.sleep(2)

    def search(self):
        search_btn = self.driver.find_element(By.CLASS_NAME, 'sb-searchbox__button')
        search_btn.click()
        time.sleep(5)

    def set_dates(self):
        # TODO: select dates in the middle of the period
        datepicker_path = "//td[@role='gridcell']"
        datepicker = self.driver.find_elements(By.XPATH, datepicker_path)
        datepicker[30].click()
        datepicker[31].click()

    def set_adults_count(self):
        adults_area = self.driver.find_element(By.CLASS_NAME, 'xp__guests')
        adults_area.click()
        time.sleep(1)
        adults_btn = self.driver.find_element(By.CLASS_NAME, 'bui-stepper__subtract-button')
        adults_btn.click()

    def select_all_pages(self):
        pagination_elements = self.driver.find_elements(By.TAG_NAME, "ol")
        pages_cnt = self.get_pages_count(pagination_elements)

        self.driver.execute_script("window.scrollTo(0, 800);")

        for page_number in range(2, pages_cnt + 1):
            btn_path = f"//button[@aria-label=' {str(page_number)}']"
            next_page_btn = self.driver.find_element(By.XPATH, btn_path)
            next_page_btn.click()
            time.sleep(2)

            yield

            self.driver.execute_script("window.scrollTo(0, 800);")

    def get_pages_count(self, pagination_elements):
        elements = [el.text for el in pagination_elements if el.text.startswith('1\n')]
        if len(elements) == 1:
            pages_cnt = elements[0].split('\n')
            return int(pages_cnt[-1])
        return None

    def collect_data_by_page(self):
        for _ in self.select_all_pages():
            properties = self.property_parser.parse()
            database.save_properties(properties, self.city)
