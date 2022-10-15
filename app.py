# Import flask and render_template
from flask import Flask, render_template
import os

# Create your application object
app = Flask(__name__)

# Use the decorator pattern to
# link the view function to a url
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.route('/')
def home():
    
    return render_template('index.html')  # return a string

# Start the development server using the run() method
if __name__ == '__main__':
    app.run()