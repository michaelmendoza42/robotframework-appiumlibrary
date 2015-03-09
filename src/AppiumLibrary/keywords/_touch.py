# -*- coding: utf-8 -*-

from appium.webdriver.common.touch_action import TouchAction
from AppiumLibrary import utils
from AppiumLibrary.locators import ElementFinder
from keywordgroup import KeywordGroup

class _TouchKeywords(KeywordGroup):

    def __init__(self):
        self._element_finder = ElementFinder()

    # Public, element lookups
    def zoom(self, locator, percent="200%", steps=1):
        """
        Zooms in on an element a certain amount.
        """
        driver = self._current_application()
        element = self._element_find(locator, True, True)
        driver.zoom(element=element, percent=percent, steps=steps)

    def pinch(self, locator, percent="200%", steps=1):
        """
        Pinch in on an element a certain amount.
        """
        driver = self._current_application()
        element = self._element_find(locator, True, True)
        driver.pinch(element=element, percent=percent, steps=steps)

    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        """
        Swipe from one point to another point, for an optional duration.
        """
        driver = self._current_application()
        driver.swipe(start_x, start_y, end_x, end_y, duration)

    def scroll(self, start_locator, end_locator):
        """
        Scrolls from one element to another
        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.
        """
        el1 = self._element_find(start_locator, True, True)
        el2 = self._element_find(end_locator, True, True)
        driver = self._current_application()
        driver.scroll(el1, el2)

    def long_press(self, locator):
        """ Long press the element """
        driver = self._current_application()
        element = self._element_find(locator, True, True)
        long_press = TouchAction(driver).long_press(element)
        long_press.perform() 

    def tap_element(self, locator):
        """ Tap on element """
        driver = self._current_application()
        el = self._element_find(locator, True, True)
        action = TouchAction(driver)
        action.tap(el).perform()
        
    def tap(self, x, y, duration=None):
        """
        Taps the location of the given coordinates. If the coordinates
        entered are decimal values, they are interpreted as percentages of
        the screen width and height."""
        driver = self._current_application()
        window_size = driver.get_window_size()
        x = float(x)
        y = float(y)
        if (x < 1):
            x = round(x*float(window_size['width']))
        if (y < 1):
            y = round(y*float(window_size['height']))
        self._info("Tapping coordinates: %d, %d." % (x, y))
        driver.tap([(x,y)], duration)
