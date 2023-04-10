from flask import *
import requests

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    data = response.json()
    meme_large = data['preview'][3]
    print(data['preview'][3])
    return meme_large

app = Flask(__name__)

@app.route("/")
def index():
    meme_pic=get_meme()
    return render_template("meme_index.html",meme_pic=meme_pic)

@app.route("/floppa")
def floppin():
    return "placegolder - in future there will be a floppa"

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "<h1><center>404 - ඞ sus erorr</center></h1>", 404
app.run(host="0.0.0.0",port=81)