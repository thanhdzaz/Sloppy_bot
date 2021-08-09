from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return ('còn sống nè nè!!');

def run():
  app.run(host='0.0.0.0',port=8080)

def Alive():
  t = Thread(target=run)
  t.start()
