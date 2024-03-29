# -*- coding: utf-8 -*-
"""day_26.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vEEuhvGrfo4F7u7JCM67g37sv3c97TFT
"""



"""Python for Web

Python is a general purpose programming language and it can be used for many places. In this section, we will see how we use Python for the web. There are many Python web frame works. Django and Flask are the most popular ones. Today, we will see how to use Flask for web development.

Flask

Flask is a web development framework written in Python. Flask uses Jinja2 template engine. Flask can be also used with other modern front libraries such as React.

If you did not install the virtualenv package yet install it first. Virtual environment will allows to isolate project dependencies from the local machine dependencies.

pip install virtualenv
"""



from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello, this is our first flask website";  
  
if __name__ =='__main__':  
    app.run(debug = True)





"""Flask App routing

App routing is used to map the specific URL with the associated function that is intended to perform some task. It is used to access some particular page like Flask Tutorial in the web application.

In our first application, the URL ('/') is associated with the home function that returns a particular string displayed on the web page.

In other words, we can say that if we visit the particular URL mapped to some particular function, the output of that function is rendered on the browser's screen.
"""

from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home')  
def home():  
    return "hello, welcome to our website";  
  
if __name__ =="__main__":  
    app.run(debug = True)

"""Flask Templates

In the previous examples, we have returned the simple string as the response from the view function. Although, flask facilitates us to return the response in the form of HTML templates. In this section of the tutorial, we will go through the ways using which we can return the HTML response from the web applications.

from flask import *  
app = Flask(__name__)  
@app.route('/')  
def message():  
      return "<html><body><h1>Hi, welcome to the website</h1></body></html>"  
if __name__ == '__main__':  
   app.run(debug = True)
"""