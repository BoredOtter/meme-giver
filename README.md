# FirstFlaskApp

This repository contains a Flask-based meme generator web application that retrieves JSON files contaings information about memes from the meme-api.com API (meme-api.com/gimme) which is scrapping memes from reddit. It also includes a Dockerfile to enable easy containerization and deployment of the application.
### Using localy
1. Run loccaly by runing app.py
2. Enter http://localhost/ in your web browser
### Using as docker image
1. Create docker image:
2. `docker build -t python-meme-one`
3. `docker run -p 80:5000 python-meme-on`
4. Enter http://localhost/ in your web browser
