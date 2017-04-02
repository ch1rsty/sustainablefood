from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
app=Flask(__name__)

app = Flask("SustainableFood")

@app.route('/')
def home():
    return render_template('index.html')

jannettas = 0

@app.route("/search", methods=['POST'])
def search():
    form_data = request.form
    print form_data['location']
    print form_data['dietary']
    print form_data['cuisine']
    print form_data['price']


    
    if form_data['location'] in open('jannettas.txt').read():
                                 return true

    return false

if __name__ == '__main__':
    app.run()
