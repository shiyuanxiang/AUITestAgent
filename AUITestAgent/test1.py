import requests
#
# app_package = 'com.example.wick'
# app_activity = 'com.example.wick.MainActivity'
# data = {
#     "app_package": app_package,
#     "app_activity": app_activity
# }
# response = requests.post('http://localhost:5001/start_driver', json=data)
# print(response.json())

# response = requests.get('http://localhost:5001/status')
# print(response.json())

response = requests.post('http://localhost:5001/stop_driver', json={})
print(response.json())