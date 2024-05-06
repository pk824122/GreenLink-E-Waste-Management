# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 06:25:31 2021

@author
"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/aboutus')
def index():
    return render_template('About.html')

@app.route('/')
def index1():
    return render_template('Main.html')

@app.route('/home')
def index2():
    return render_template('Main.html')
                           
@app.route('/faqs')
def index3():
    return render_template('Faqs.html')

@app.route('/login')
def index4():
    return render_template('LoginClient.html')

@app.route('/productfull')
def index5():
    return render_template('Product full.html')

@app.route('/contact')
def index6():
    return render_template('Contact client.html')



if __name__ == '__main__':
    app.run()