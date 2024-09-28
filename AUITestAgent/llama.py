import random

import requests
import json

class Chatllama:
    def __init__(self, prompt, model="llama3.1-ft:latest"):
        """
        :param prompt: list
        :param model:
        """
        self.messages = prompt
        self.status = "running"
        self.llama_chat_url = "http://10.103.11.105:11434/api/chat"
        self.model = model

    def chat(self, new_message, widgets_str):
        """
        :param new_message:{
            "role": "user",
            "content": {
                "task": "",
                "action_history": [""],
                "current_activity": "",
                "widgets": [],
            }.__str__()
        }
        :param widgets_str:
        :return: the actions that llama suggests. [{"action":"", "target":"", "input_text":""}, ...]
        """
        seed = random.randint(0, 1000)
        self.messages.append(new_message)
        data = {
            "model": self.model,
            "messages": self.messages,
            "stream": False,
            "seed": 685,
            "temperature": 0
        }
        print(f"[input] {data}")
        response = requests.post(self.llama_chat_url, data=json.dumps(data))
        self.messages.append(response.json()["message"])
        print(f"[response] {response.json()['message']}")
        return self.parse_response_02(response, widgets_str)

    def parse_response_01(self, response, widgets_str):
        """
        :param response:
        :param widgets:
        :return:
        """
        suggest_actions = []
        content = response.json()['message']['content'].replace("\n", " ")
        action_number = int(content.split(";")[0].split(":")[1].strip())
        for ac in content.split(";")[1:]:
            ac = ac[2:]
            action_type = ac.split(" on ")[0].strip().split(".")[1].strip()
            target = ""
            if " on " in ac:
                target = ac.split(" on ")[1].split(" with ")[0].strip()
            input_text = ""
            if " with " in ac:
                input_text = ac.split(" with ")[1].split("]")[0].strip()
            # filter the valid actions (show in current activity)
            if target in widgets_str:
                suggest_actions.append(
                    {
                        "action": action_type,
                        "target": target,
                        "input_text": input_text,
                    }
                )
        return suggest_actions


    def parse_response_02(self, response, widgets_str):
        suggest_actions = []
        actions = json.loads(response.json()['message']['content'].replace("'", "\""))
        for ac in actions:
            if ac['target'] in widgets_str or ac['action'] == 'back':
                suggest_actions.append(ac)
        return suggest_actions
