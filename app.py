import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://meme-api.com/gimme/70"
    response = requests.get(url)
    memes = response.json()["memes"]
    return render_template("home.html", MEMES=memes)


if __name__ == '__main__':
    app.run(debug=False)