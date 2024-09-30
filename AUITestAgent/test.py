import requests

response = requests.post('http://localhost:5001/start_driver',
                         json={'app_package': 'com.example.wick', 'app_activity': '.MainActivity'})

response = requests.get('http://localhost:5001/get_page_source')
print(response.json())
# response = requests.post('http://localhost:5001/scroll_all', json={'scroll_terms': 3})


response = requests.post('http://localhost:5001/execute_action',
                         json={"action": "click", "target": "com.example.wick:id/ContentProviderTestBt", "input_text": ""})


response = requests.post('http://localhost:5001/execute_action',
                         json={"action": "input", "target": "com.example.wick:id/name", "input_text": "hello"})


print(response.json())

