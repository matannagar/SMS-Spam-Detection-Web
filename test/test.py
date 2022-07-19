import requests 

# https://your-heroku-app-name.herokuapp.com/predict
# http://localhost:5000/predict
resp = requests.post("https://flask-smsphishing.herokuapp.com/predict", data={'sms': 'you are a wizard!'})

print(resp.text)