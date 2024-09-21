class Selector:
    def __init__(self, observer, history):
        self.observer = observer
        self.history = history

    def select(self):
        user_prompt = self.make_user_prompt()
        assistant_response = self.make_assistant_response(user_prompt)
        return assistant_response

    def make_user_prompt(self):
        user_prompt = {"role": "user", "content": {}}
        user_prompt["content"]["task"] = self.history.get_task()
        user_prompt["content"]["action_history"] = self.history.get_action_history()
        user_prompt["content"]["current_activity"] = self.observer.get_current_activity()
        user_prompt["content"]["widgets"] = self.observer.get_ui_hierarchy()
        return user_prompt

    def make_assistant_response(self, user_prompt):
        """
        Using fine-tuned llm model to generate assistant response.
        :param user_prompt:
        :return: {
                  "role": "assistant",
                  "content": [
                    {
                      "action": "",
                      "target": "",
                      "input_text": ""
                    }
                  ]
                }
        """
        assistant_response = {"role": "assistant", "content": []}
        # todo: using llm to generate response
        return assistant_response
