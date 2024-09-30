import requests
import xml.etree.ElementTree as ET


class Observer:
    def __init__(self):
        self.ui_hierarchy = []

    def widgets_prompt(self):
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
        response = requests.get('http://localhost:5001/get_page_source')
        if response.status_code != 200:
            return self.ui_hierarchy
        page_source = response.json()['page_source']
        root = ET.fromstring(page_source)
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

        self.widgets_prompt()
        return self.ui_hierarchy

    def get_current_activity(self):
        response = requests.get('http://localhost:5001/get_current_activity')
        if response.status_code == 200:
            return response.json()['current_activity']
        return None
