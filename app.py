# Import flask and render_template
from flask import Flask, render_template, request
import os
from Main import *

# Create your application object
app = Flask(__name__)
conversation = []
times = []
texts = dict(zip(conversation, times))
converation = []
response = "Hi, I'm Violet. It's so nice to meet you today!"
m = Main()
# Use the decorator pattern to
# link the view function to a url
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.route('/home')
def home():
    return render_template('home.html') 

@app.route('/')
def index():
    data = {"conversation":conversation}
    return render_template('index.html', data=data) 

@app.route('/sendmessage', methods=["POST"])
def sendmessage():
    data = request.get_json()
    data = str(data)
    data = data[data.find("lastmsg=")+8:]
    data = data[:data.find("'")]
    data = data.replace("+"," ")
    conversation.append(data)
    response = m.main(conversation)
    conversation.append(response)
    print(conversation)
    return "E"


@app.route('/', methods=["POST"])
def index_form():
    print(request.form['lastmsg'])
    return render_template('index.html') 

@app.route('/login/')
def login():
    return render_template('login.html') 

@app.route('/about/')
def about():
    return render_template('about.html') 

@app.route('/access/')
def access():
    return render_template('access.html') 

# Start the development server using the run() method
if __name__ == '__main__':
    app.run(debug=True)