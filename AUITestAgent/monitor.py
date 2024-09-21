class Monitor:
    def __init__(self, observer, history):
        self.observer = observer
        self.history = history

    def tell_if_done(self):
        """
        Tell if the task is done.
        :return: bool
        """
        task = self.history.get_task()
        ui_hierarchy = self.observer.get_ui_hierarchy()
        action_history = self.history.get_action_history()
        current_activity = self.observer.get_current_activity()
        # todo: using llm to check if the task is done.
        return False
