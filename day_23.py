# -*- coding: utf-8 -*-
"""day 23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ttc3gr8VhSx1IJ1E4eAXNX49Mj2Y19kE
"""

pip install virtualenv

python -m venv venv



"""What is Flask?

Flask is a web framework that provides libraries to build lightweight web applications in python. It is developed by Armin Ronacher who leads an international group of python enthusiasts (POCCO). It is based on WSGI toolkit and jinja2 template engine. Flask is considered as a micro framework.

What is WSGI?

It is an acronym for web server gateway interface which is a standard for python web application development.
"""



$ pip install virtualenv

Once it is installed, we can create the new virtual environment into a folder as given below.

$ mkdir new   
$ cd new   
$ virtualenv venv

To activate the corresponding environment, use the following command on the Linux operating system.

$ venv/bin/activate

On windows, use the following command.

$ venv\scripts\activate

We can now install the flask by using the following command.

$ pip install flask

pip freeze

deactivate