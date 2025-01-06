from flask import Flask
'''
It create a instance of class flask ,
which will be our WSGI application

'''
app=Flask(__name__)
'''
___name__ is the entry for python and  it will run from that (entry point )
'''
@app.route("/")
def welcome():
    return "Welcome to this course flask123"

@app.route("/index")
def index():
    return "Welcome to this index page"

if __name__=="__main__":
    app.run(debug=True) # debug=True is helpfull to make like nodemon no need to no need to run again again file 
