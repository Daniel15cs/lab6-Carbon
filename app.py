from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "<h1> Hello world from Azure with python by Danylo Kyrychenko for lab6 using git!V1</h1>"
 # ""<p> Виконав Кириченко Данило Романович</p>"

if __name__ == '__main__':
    app.run()
