'''
Created on Nov 27, 2024

@author: admin
'''
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# We defined string  function
@app.route('/vstring/<name>')
def string(name):
    return "My Name is %s" % name
 
# we run app debugging mode
app.run(debug=True)


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()