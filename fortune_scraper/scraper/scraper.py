from __future__ import print_function
from flask import Flask
import urllib
import json
import random
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

fortune_url = "http://dojodevopschallenge.s3-website-eu-west-1.amazonaws.com/fortune_of_the_day.json"
fortune_message = None

def scraper():
    global fortune_message
    response = urllib.urlopen(fortune_url)
    data = json.loads(response.read())
    quote = random.choice(data)
    fortune_message = quote['message']

sched = BackgroundScheduler(daemon=True)
sched.add_job(scraper,'interval',seconds=10)
sched.start()
scraper()
    
@app.route('/')
def index():
    return fortune_message

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')