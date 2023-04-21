from flask import Flask, render_template,redirect, url_for
import requests

app = Flask(__name__)

def get_meme():
    try:
        response = requests.get('https://meme-api.com/gimme')
        data = response.json()
        #print(data)
        meme_large = data['preview'][3]
        message = "From: r/"+data['subreddit']
        return meme_large,message
    except:
        #print("somethings broken")
        meme_large="https://i.kym-cdn.com/photos/images/original/002/028/689/381.jpg"
        message="something's broken with api (i think), so u can get floppa"
        return meme_large,message



@app.route('/',methods=['GET', 'POST'])
def root():
    return render_template("index.html")

@app.route('/meme')
def meme():
    meme_pic,message=get_meme()
    return render_template("meme.html",meme_pic=meme_pic,message=message)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)