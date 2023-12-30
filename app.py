from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

def get_meme():
    try:
        response = requests.get('https://meme-api.com/gimme')
        data = response.json()
        #print(data)

        if('preview' in data):
            preview_length = len(data['preview'])
            if preview_length > 3:
                meme_large = data['preview'][3]
            else:
                index = min(2, preview_length - 1)
                meme_large = data['preview'][index]
        else:
            raise Exception("No proper data received")

        message = "From: r/"+data['subreddit']
        return meme_large,message
    except:
        #print("somethings broken")
        meme_large="https://i.kym-cdn.com/photos/images/original/002/028/689/381.jpg"
        message="something's broken with api (i think), so u can get floppa :333"
        return meme_large,message



@app.route('/')
def meme():
    meme_pic,message=get_meme()
    return render_template("meme.html",meme_pic=meme_pic,message=message)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/k8s')
def k8s():
    env_vars = {
        'HOSTNAME': os.getenv('HOSTNAME'),
        'KUBERNETES_PORT': os.getenv('KUBERNETES_PORT')
    }
    return jsonify(env_vars)

if __name__ == '__main__':
    app.run(debug=False)