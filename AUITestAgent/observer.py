from selenium.webdriver.common.by import By

from AUITestAgent.driver_helper import DriverHelper
import xml.etree.ElementTree as ET


class Observer:
    def __init__(self):
        self.ui_hierarchy = []

    def prompt(self):
        tmp_list = []
        for widget in self.ui_hierarchy:
            if widget['actions'] != "":
                tmp_list.append(f"{widget['id']} with text \'{widget['text']}\' is a "
                                f"{widget['category']} which can be {widget['actions']}.")
        self.ui_hierarchy = tmp_list.copy()

    def get_ui_hierarchy(self):
        """
        Get the UI hierarchy of the current screen
        :return: ["<text> is a <category> which can be <actions>",...]
        """
        self.ui_hierarchy = []
        driver = DriverHelper.get_driver()

        if_scrollable = False
        elements = driver.find_elements(By.XPATH, "//*")
        for element in elements:
            if element.get_attribute("scrollable") == "true":
                if_scrollable = True
                break
        if if_scrollable:
            DriverHelper.scroll_all()
            
        root = ET.fromstring(driver.page_source)
        action_types = ["checkable", "checked", "clickable", "focusable", "long-clickable", "scrollable", "selected"]
        for child in root.iter():
            widget_info = {
                "text": child.attrib.get('text'),
                "id": child.attrib.get('resource-id'),
                "category": child.attrib.get('class'),
                "actions": ""
            }
            tmp_list = []
            for at in action_types:
                if child.attrib.get(at) == "true":
                    tmp_list.append(at)
            widget_info["actions"] = ", ".join(tmp_list)
            self.ui_hierarchy.append(widget_info)

        self.prompt()
        return self.ui_hierarchy

    def get_current_activity(self):
        driver = DriverHelper.get_driver()
        return driver.current_activity
