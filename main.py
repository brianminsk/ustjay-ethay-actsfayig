import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

pig_latin_post_url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"

def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText().strip()


def get_pig_latin_url(text):
    request = requests.post(pig_latin_post_url, data = {'input_text':text})
    return url


@app.route('/')
def home():
    fact = get_fact()
    url = get_pig_latin_url(fact)
    return url


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

