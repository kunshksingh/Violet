# Import flask and render_template
from flask import Flask, render_template, request
import os

# Create your application object
app = Flask(__name__)
conversation = []
times = []
texts = dict(zip(conversation, times))
# Use the decorator pattern to
# link the view function to a url
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.route('/home')
def home():
    return render_template('home.html') 

#@app.route('/', methods=["GET", "POST"])
@app.route('/')
def index():
    conversation = []
    #rf = request.json
    #print(rf)
    #for key in rf.keys():
        #data = key
    #print(data)
    #data_dic = json.loads(data)
    #print(data_dic.keys())
    #sum_data = data_dic['sum']
   #if request.method == "POST":
    msgs = request.form.get('msgs')
    print(msgs)
    #Message = {"Message": msgs}
    return render_template('index.html', msgouts=msgs) 



    # userText = request.args.get("lastmsg")
    # print(userText)
    #print("referes")




#@app.route('/', methods=['GET', 'POST'])
#def index_form():
    #print(request.form['lastmsg'])
    #userText = request.args.get('input')
    #print(userText)
    #return render_template('index.html') 
'''
@app.route('/', methods=['POST'])
def get_response():
    #print(request.form['lastmsg'])
    userText = request.get['lastmsg']
    print(userText)
    print("efefefs")
    return
'''
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
if __name__ == 'main':
    app.run()