import time

from selenium.webdriver.common.by import By

from Api_Operations.Requests_Operations import Request_Operations
from Selenium_Operations.Element_Operations import Element_Operations


class Customer_APIs(Request_Operations):
    def __init__(self, base_url):
        self.base_url = base_url
        Request_Operations.__init__(self, self.base_url)


