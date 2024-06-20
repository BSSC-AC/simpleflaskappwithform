# Author: Warren Sutton , Date 20 Jun 2024
# This is intended as a very simple flask application with just a single file
# required. I've deliberately avoided the use of a HTML template file which would
# require the render_template library. I've also avoided the use of Jinja.
# The html utilised is very simple, and the program utilses neither
# CSS nor JavaScript.
# I use a very simple 'list' data structure and a HTML form to allow
# for the input of data. The intent was to show students, who are familiar with
# Python and tkinter, how they might use Flask to develop GUI for a programming
# task.

from flask import Flask, request

app = Flask(__name__)
names = ['fred', 'bob', 'tom']


@app.route('/')
def index():
    return '''
  <H1>Warren's big party list kkkk</H1>
  <br>
  <a href="/book">add another guest </a>
  <br>
  <a href="/list">list all those who have confirmed </a>
  <br>  
  '''

@app.route('/book', methods=["POST", "GET"])
def book():
    if request.method == 'POST':
        gname = request.form["name_input"]
        names.append(gname)
        return '''
    <H1>You have added... </H1>
    <br>''' + gname + '''
    <H2>to your party list</H2>
    <br>
    <a href="/">return to home page</a>'''

    if request.method == 'GET':
        return '''
    <H1>Add more people to the big party list</H1>
    <form action="/book" method="post">
    <br>
    <input type="text" name="name_input">
    <br>
    <input type="submit" value="Click here"/>
    </form>
    <br>
    <a href="/">return to home page</a>
    '''


@app.route('/list')
def list():
    # produces the list of people as a string in HTML format
    name_list = ''
    for name in names:
        name_list = name_list + '<p>' + name + '</p>'

    return '''
  <H1>The list of everyone who will be attending your party!</H1>''' + name_list + '''
  <br>
  <a href="/">return to home page</a>
  '''

if __name__ == '__main__':
    app.run(debug=True)