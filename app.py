from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "<h1> Hello world from Azure with python by Danylo Kyrychenko for lab6 using git and nvim btw! </h1>"

if __name__ == '__main__':
    app.run()
