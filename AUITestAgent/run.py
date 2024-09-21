from AUITestAgent.executor import Executor
from AUITestAgent.history import History
from AUITestAgent.monitor import Monitor
from AUITestAgent.observer import Observer
from AUITestAgent.selector import Selector


def main():
    task = "test"
    observer = Observer()
    history = History(task)
    selector = Selector(observer, history)
    executor = Executor(history)
    monitor = Monitor(observer, history)
    while True:
        assistant_response = selector.select()
        executor.execute(assistant_response)
        if monitor.tell_if_done():
            break


if __name__ == '__main__':
    main()
