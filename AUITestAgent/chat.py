import requests
import json

messages = [
    {
        "role": "system",
        "content": "The format of your answer should be like 'The number of actions: <action_number>; 1. <action_type> on <widget> [with <input_text>]; 2. ...'. The <widget> in your answer must be one of the widgets I provied, and use 'on' instead of 'into' or other verbs for 'input' action."
    },
    {
        "role": "system",
        "content": "'[with <input_text>]' is optional, if there is no input text, you can omit it, otherwise you should provide it. For example, 'click on com.example.wick:id/ContentProviderTestBt' is a valid answer. 'input on com.example.wick:id/name with ai01' is also a valid answer."
    },
    {
        "role": "system",
        "content": "Your answer should be strictly in the format I provided, starts with 'The number of actions: ...', otherwise I may not be able to parse it correctly."
    },
    {
        "role": "user",
        "content": {
            "task": "In the content provider view, input a student info with name='ai01' and grade='A', then click 'Add Item'. Check if there is a Toast showing with text starts with 'added'.",
            "action_history": [],
            "current_activity": "com.example.wick.MainActivity",
            "widgets": [
                "com.example.wick:id/getAccount with text 'Get Account' is a android.widget.Button which can be clickable, focusable.",
                "com.example.wick:id/goToActivity with text 'Go To Activity' is a android.widget.Button which can be clickable, focusable.",
                "com.example.wick:id/nextActivity with text 'Next Activity' is a android.widget.Button which can be clickable, focusable.",
                "com.example.wick:id/activityInfo with text 'Activity Info' is a android.widget.Button which can be clickable, focusable.",
                "com.example.wick:id/BroadcastTest with text 'BroadcastTest' is a android.widget.Button which can be clickable, focusable.",
                "com.example.wick:id/ContentProviderTestBt with text 'ContentProviderTest' is a android.widget.Button which can be clickable, focusable.",
                "com.example.wick:id/ServiceTest with text 'ServiceTest' is a android.widget.Button which can be clickable, focusable.",
                "com.example.wick:id/button8 with text 'Button 8' is a android.widget.Button which can be clickable, focusable.",
            ],
        }.__str__(),
    },
    {
        "role": "assistant",
        "content": [
            {
                "action": "click",
                "target": "com.example.wick:id/ContentProviderTestBt",
                "input_text": "",
            }
        ].__str__(),
    },
    {
        "role": "user",
        "content": {
            "task": "In the content provider view, input a student info with name='ai01' and grade='A', then click 'Add Item'. Check if there is a Toast showing with text starts with 'added'.",
            "action_history": ["click on com.example.wick:id/ContentProviderTestBt"],
            "current_activity": "com.example.wick.ContentProviderTestActivity",
            "widgets": [
                "com.example.wick:id/name with text 'Name' is a android.widget.EditText which can be clickable, focusable, long-clickable.",
                "com.example.wick:id/grade with text 'Grade' is a android.widget.EditText which can be clickable, focusable, long-clickable.",
                "com.example.wick:id/updateButton with text 'Update Item' is a android.widget.Button which can be clickable, focusable.",
                "com.example.wick:id/deleteButton with text 'Del Item' is a android.widget.Button which can be clickable, focusable.",
                "com.example.wick:id/addItemButton with text 'Add Item' is a android.widget.Button which can be clickable, focusable.",
                "com.example.wick:id/queryButton with text 'Query' is a android.widget.Button which can be clickable, focusable.",
            ],
        }.__str__(),
    },
    {
        "role": "assistant",
        "content": [
            {
                "action": "input",
                "target": "com.example.wick:id/name",
                "input_text": "ai01",
            },
            {
                "action": "input",
                "target": "com.example.wick:id/grade",
                "input_text": "A",
            },
            {
                "action": "click",
                "target": "com.example.wick:id/addItemButton",
                "input_text": "",
            },
        ].__str__(),
    },
]


class Chatllama:
    def __init__(self, prompt, model="llama3.1-ft:latest"):
        self.messages = prompt
        self.status = "running"
        self.llama_chat_url = "http://10.103.11.105:11434/api/chat"
        self.model = model
        self.action_history = []

    def chat(self, new_message, if_ft=False):
        self.messages.append(new_message)
        data = {
            "model": self.model,
            "messages": self.messages,
            "stream": False,
        }
        response = requests.post(self.llama_chat_url, data=json.dumps(data))
        self.messages.append(response.json()["message"])
        return response

    def parse_response(self, response):
        content = response.json()['message']['content']
        print(f"[Content]: {content}")
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
            print(f"[Action]: {action_type}, [Target]: {target}, [Input Text]: {input_text}")
            self.action_history.append(
                {
                    "action": action_type,
                    "target": target,
                    "input_text": input_text,
                }
            )

    def run(self):
        while True:
            task = input("[Task]: (input 'stop' to stop, input 'ft' to fine tune.) ")
            if task == "stop":
                break
            new_message = {"role": "user", "content": ""}
            if task == "ft":
                new_message["content"] = input("[FT Message]: ")
            else:
                current_activity = input("[Current Activity]: ")
                widgets = input("[Widgets]: (split by ';') ")
                widgets = widgets.split(";")

                new_message["content"] = (
                    {
                        "task": task,
                        "action_history": self.action_history,
                        "current_activity": current_activity,
                        "widgets": widgets,
                    },
                )
                new_message["content"] = new_message["content"][0].__str__()
            response = self.chat(new_message)
            print(f"[Messages]: {self.messages}")
            self.parse_response(response)
            print(f"[Assistant]: {response.json()['message']}")


if __name__ == "__main__":
    chatllama = Chatllama(messages)
    chatllama.run()
