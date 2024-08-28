from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP
from utils.locators import Locators
from utils.assets import get_text_asset
from utils.rpaValidators import DataChecker
from loguru import logger


class AppController:
    def __init__(self):
        self.url = get_text_asset("URL")
        self.sort_type = get_text_asset("SORT_TYPE")
        self.output_path = get_text_asset("OUTPUT_PATH")
        self.browser = None
        self.locators = Locators()
        self.validator = DataChecker()
        self.http = HTTP()
        
        logger.add("output/logs_loguru.log", format="{time} - {level} - {message}")
        self.logger = logger

    def initialize(self):
        self.browser = Selenium()
        self.browser.open_available_browser(self.url)
        self.browser.maximize_browser_window()

    def end_process(self):
        self.browser.close_browser()