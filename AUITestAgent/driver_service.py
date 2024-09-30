from flask import Flask, jsonify, request
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

app = Flask(__name__)
driver = None


@app.route('/start_driver', methods=['POST'])
def start_driver():
    global driver
    options = UiAutomator2Options()
    options.platform_name = request.json.get('platform_name', 'Android')
    options.platform_version = request.json.get('platform_version', '14')
    options.device_name = request.json.get('device_name', '43141JEKB03040')
    options.app_package = request.json.get('app_package')
    options.app_activity = request.json.get('app_activity')
    options.new_command_timeout = 6000

    try:
        driver = webdriver.Remote('http://localhost:4723', options=options)
        return jsonify({'message': 'Driver started successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/stop_driver', methods=['POST'])
def stop_driver():
    global driver
    if driver:
        driver.quit()
        # driver = None
        return jsonify({'message': 'Driver stopped successfully'}), 200
    else:
        return jsonify({'error': 'No driver instance found'}), 404


@app.route('/status', methods=['GET'])
def status():
    global driver
    if driver:
        return jsonify({'status': 'Driver is running'}), 200
    else:
        return jsonify({'status': 'Driver is not running'}), 404


@app.route('/get_page_source', methods=['GET'])
def get_page_source():
    global driver
    if driver:
        page_source = driver.page_source
        if_scrollable = False
        elements = driver.find_elements(By.XPATH, "//*")
        for element in elements:
            if element.get_attribute("scrollable") == "true":
                if_scrollable = True
                break
        if if_scrollable:
            # todo: to be tested.
            scroll_all()
        return jsonify({'page_source': page_source}), 200
    else:
        return jsonify({'error': 'No driver instance found'}), 404


@app.route('/scroll_all', methods=['POST'])
def scroll_all():
    global driver
    if driver:
        scroll_terms = request.json.get('scroll_terms', 3)
        end_y = driver.get_window_size()['height'] / 3
        start_y = driver.get_window_size()['height'] * 2 / 3
        _x = driver.get_window_size()['width'] / 2
        for i in range(scroll_terms):
            driver.swipe(start_x=_x, start_y=start_y, end_x=_x, end_y=end_y, duration=500)
        return jsonify({'message': 'Scrolled successfully'}), 200
    else:
        return jsonify({'error': 'No driver instance found'}), 404


@app.route('/execute_action', methods=['POST'])
def execute_action():
    """
    Execute the action.
    :param action:
            {
              "action": "click",
              "target": "com.example.wick:id/page1",
              "input_text": ""
            }
    :return: None
    """
    global driver
    action = request.json
    if action["action"] == "back":
        driver.back()
        return jsonify({'message': 'Backed successfully'}), 200

    ele = driver.find_element(By.ID, action["target"])
    if action["action"] == "click":
        ele.click()
    elif action["action"] == "input":
        ele.clear()
        ele.send_keys(action["input_text"])
    elif action["action"] == "scroll":
        scroll_all({"scroll_terms": 1})
    else:
        return jsonify({'error': f"Unsupported action: {action['action']}"}), 400

    return jsonify({'message': f'Executed {action["action"]} successfully'}), 200


@app.route('/get_current_activity', methods=['GET'])
def get_current_activity():
    global driver
    if driver:
        return jsonify({'current_activity': driver.current_activity}), 200
    else:
        return jsonify({'error': 'No driver instance found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
