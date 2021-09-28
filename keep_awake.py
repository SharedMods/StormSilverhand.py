from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hey I am Still adventuring!"
def run():
  app.run(host='0.0.0.0',port=8080)
def keep_awake():
    t = Thread(target=run)
    t.start()