from executor import Executor
from history import History
from monitor import Monitor
from observer import Observer
from selector import Selector
import requests

def main():
    # task = "In the MainActivity, click ContentProviderTestBt, add an item with name='wick' and grade='007'"
    # task = ("In the MainActivity, click ContentProviderTestBt, query if there is "
    #         "an item with name='wick' and grade='007'")
    task = ("In the MainActivity, click toToSelectorTestBt, then in the new activity, click 'page1' button, go to the page1 view, then click 'page2' button"
            ", go to the page2 view, in the page2 view, click 'register', then go back to the selector view and click "
            "'done' button. Check if the text in 'status' textview changes into 'status: register'.")
    # response = requests.post('http://localhost:5001/start_driver',
    #                          json={'app_package': 'com.example.wick', 'app_activity': '.MainActivity'})
    observer = Observer()
    history = History(task)
    selector = Selector(observer, history)
    executor = Executor(observer, history)
    monitor = Monitor(observer, history)
    while True:
        suggest_actions = selector.select()
        print(f"[activity] {observer.get_current_activity()}")
        print(f"[action history] {history.get_action_history()}")
        print(f"[suggest actions] {suggest_actions}")
        executor.execute(suggest_actions)
        if monitor.tell_if_done():
            break


if __name__ == "__main__":
    main()
